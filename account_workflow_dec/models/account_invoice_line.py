# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.depends("price_unit", "discount")
    def _compute_price_reduce(self):
        for line in self:
            line.price_reduce = line.price_unit * (1.0 - line.discount / 100.0)

    price_reduce = fields.Float(
        compute="_compute_price_reduce",
        string="Price Reduce",
        digits="Product Price",
        readonly=True,
        store=False,
    )

    # TODO: [MIG] 13.0
    date_invoice = fields.Date(
        related="move_id.invoice_date",
        store=True,
        readonly=True,
    )
    # TODO: [MIG] 13.0
    commercial_partner_id = fields.Many2one(
        related="move_id.partner_id.commercial_partner_id",
        store=True,
        readonly=True,
        compute_sudo=True,
    )
    # TODO: [MIG] 13.0
    state = fields.Selection(
        related="move_id.state",
        store=True,
        readonly=True,
        string="Invoice State",
    )
    # TODO: [MIG] 13.0
    invoice_number = fields.Char(
        related="move_id.name",
        store=True,
        readonly=True,
        string="Invoice Number",
    )
