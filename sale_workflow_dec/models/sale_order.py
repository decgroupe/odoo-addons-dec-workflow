# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Mar 2020

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_shipping_zip_id = fields.Many2one(
        'res.city.zip',
        'ZIP Location',
        related='partner_shipping_id.zip_id',
        readonly=True,
    )

    @api.multi
    def copy(self, default=None):
        if self.origin:
            origin = ('%s:%s') % (
                self.origin,
                self.name,
            )
        else:
            origin = self.name

        default = dict(
            default or {},
            origin=origin,
        )
        return super().copy(default)
