# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Sep 2022

from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def _compute_sales_count(self):
        # Override default implementation to remove the 365 days domain filter
        # from ./odoo/addons/sale/models/product_product.py
        r = {}
        if not self.user_has_groups('sales_team.group_sale_salesman'):
            return r

        done_states = self.env['sale.report']._get_done_states()
        domain = [
            ('state', 'in', done_states),
            ('product_id', 'in', self.ids),
        ]
        for group in self.env['sale.report'].read_group(
            domain, ['product_id', 'product_uom_qty'], ['product_id']
        ):
            r[group['product_id'][0]] = group['product_uom_qty']
        for product in self:
            product.sales_count = float_round(
                r.get(product.id, 0),
                precision_rounding=product.uom_id.rounding
            )
        return r
