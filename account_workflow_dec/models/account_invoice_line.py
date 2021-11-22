# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.depends('price_unit', 'discount')
    def _compute_price_reduce(self):
        for line in self:
            line.price_reduce = line.price_unit * (1.0 - line.discount / 100.0)

    price_reduce = fields.Float(
        compute='_compute_price_reduce',
        string='Price Reduce',
        digits=dp.get_precision('Product Price'),
        readonly=True,
        store=False,
    )

    # Following code is copied from:
    # akretion/odoo-usability/account_usability/account.py
    invoice_type = fields.Selection(store=True, )
    date_invoice = fields.Date(
        related='invoice_id.date_invoice',
        store=True,
        readonly=True,
    )
    commercial_partner_id = fields.Many2one(
        related='invoice_id.partner_id.commercial_partner_id',
        store=True,
        readonly=True,
        compute_sudo=True,
    )
    state = fields.Selection(
        related='invoice_id.state',
        store=True,
        readonly=True,
        string='Invoice State',
    )
    invoice_number = fields.Char(
        related='invoice_id.move_id.name',
        store=True,
        readonly=True,
        string='Invoice Number',
    )
