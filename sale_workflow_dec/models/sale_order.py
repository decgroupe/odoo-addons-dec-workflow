# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Mar 2020

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    # def _get_validity_date(self):
    #     for order in self:
    #         order.validity_date  = order.date_order + relativedelta(days=order.validity or 0.0)

    summary = fields.Char(
        size=128,
        help="Order summary to quickly identify this order in treeview",
    )
    # validity = fields.Integer(
    #     'Validity period',
    #     readonly=True,
    #     states={'draft': [('readonly', False)]},
    #     help="Validity delay in day(s)"
    # )
    warranty = fields.Integer(
        'Warranty period',
        readonly=True,
        states={'draft': [('readonly', False)]},
        help="Warranty delay in year(s)",
        default=2
    )
    # validity_date = fields.Date(
    #     compute=_get_validity_date,
    #     store=True,
    #     help="Date of validity"
    # )

    partner_shipping_zip_id = fields.Many2one(
        'res.city.zip',
        'ZIP Location',
        related='partner_shipping_id.zip_id',
        readonly=True,
    )
