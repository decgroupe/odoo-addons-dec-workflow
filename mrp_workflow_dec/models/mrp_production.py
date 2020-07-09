# Copyright (C) DEC SARL, Inc - All Rights Reserved.
#
# CONFIDENTIAL NOTICE: Unauthorized copying and/or use of this file,
# via any medium is strictly prohibited.
# All information contained herein is, and remains the property of
# DEC SARL and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to DEC SARL and its suppliers and may be covered by
# French Law and Foreign Patents, patents in process, and are
# protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from DEC SARL.
# Written by Yann Papouin <y.papouin@dec-industrie.com>, July 2020

from odoo import models, api, fields


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    finished_picking_ids = fields.Many2many(
        'stock.picking',
        compute='_compute_finished_picking',
        string='Pickings associated with this manufacturing order output',
    )

    finished_picking_names = fields.Text(
        compute='_compute_finished_picking',
        string='Pickings names associated with this manufacturing order output',
    )

    finished_picking_move_ids = fields.Many2many(
        'stock.move',
        compute='_compute_finished_picking',
        string=
        'Moves on pickings associated with this manufacturing order output',
    )

    @api.multi
    def _compute_finished_picking(self):
        def get_pickings(move):
            # We need to return moves and pickings so we are creating
            # two empty recordset
            move_ids = self.env['stock.move']
            picking_ids = self.env['stock.picking']
            if move.picking_id:
                move_ids = move_ids | move
                picking_ids = picking_ids | move.picking_id
            # Make a recursive call while destination moves exists
            for move in move.move_dest_ids:
                sub_move_ids, sub_picking_ids = get_pickings(move)
                move_ids = move_ids | sub_move_ids
                picking_ids = picking_ids | sub_picking_ids
            # Return as a tuple
            return move_ids, picking_ids

        for production in self:
            all_move_ids = self.env['stock.move']
            all_picking_ids = self.env['stock.picking']
            for move in production.move_finished_ids:
                move_ids, picking_ids = get_pickings(move)
                all_move_ids = all_move_ids | move_ids
                all_picking_ids = all_picking_ids | picking_ids

            production.finished_picking_names = '\n'.join(
                o.name for o in all_picking_ids
            )
            production.finished_picking_ids = all_picking_ids.ids
            production.finished_picking_move_ids = all_move_ids.ids

    @api.multi
    def _generate_moves(self):
        super(MrpProduction, self)._generate_moves()
        for production in self:
            # Assign consumable immediatly
            consu_move_ids = production.move_raw_ids.filtered(
                lambda r: r.product_type == 'consu'
            )
            consu_move_ids._action_assign()