# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, July 2020

from odoo import models, api, fields


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    product_id = fields.Many2one(domain=[('bom_count', '>', 0)], )
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
            # Enable auto_validate on all make_to_order moves, so when a
            # product is validated on reception then this move will be set to
            # done at the same time
            mto_move_ids = production.move_raw_ids.filtered(
                lambda r: r.procure_method == 'make_to_order'
            )
            for move in mto_move_ids:
                move.auto_validate = True
            # Assign consumable immediatly
            consu_move_ids = production.move_raw_ids.filtered(
                lambda r: r.product_type == 'consu'
            )
            consu_move_ids._action_assign()

    @api.depends(
        'move_raw_ids', 'is_locked', 'state', 'move_raw_ids.quantity_done'
    )
    def _compute_unreserve_visible(self):
        """
        Fixing builtin `_compute_unreserve_visible`:addons/mrp/models/mrp_production.py
        Apply same filtering on `move_raw_ids` like the one in `do_unreserve`
        """
        super()._compute_unreserve_visible()
        for order in self:
            already_reserved = order.is_locked and order.state not in (
                'done', 'cancel'
            ) and order.mapped('move_raw_ids.move_line_ids')
            any_quantity_done = any(
                [
                    m.quantity_done > 0 for m in order.move_raw_ids.
                    filtered(lambda x: x.state not in ('done', 'cancel'))
                ]
            )
            order.unreserve_visible = not any_quantity_done and already_reserved
