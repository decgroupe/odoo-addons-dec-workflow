# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Feb 2021

from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def _compute_purchased_product_qty(self):
        # Override default implementation to remove the 365 days domain filter
        # from ./odoo/addons/purchase/models/product.py
        domain = [
            ('state', 'in', ['purchase', 'done']),
            ('product_id', 'in', self.mapped('id')),
        ]
        order_lines = self.env['purchase.order.line'].read_group(
            domain, ['product_id', 'product_uom_qty'], ['product_id']
        )
        purchased_data = dict(
            [
                (data['product_id'][0], data['product_uom_qty'])
                for data in order_lines
            ]
        )
        for product in self:
            product.purchased_product_qty = float_round(
                purchased_data.get(product.id, 0),
                precision_rounding=product.uom_id.rounding
            )

    @api.model
    def get_default_market_bom_products(self):
        res = super().get_default_market_bom_products()
        product_xmlids = [
            "product_workflow_dec.beq_workforce",
            "product_workflow_dec.beq_research_specific_development",
            "product_workflow_dec.beq_workshop_commissioning_tests"
        ]
        for product_xmlid in product_xmlids:
            product_id = self.env.ref(product_xmlid, raise_if_not_found=False)
            if product_id:
                res += product_id
        return res

    @api.model
    def get_market_bom_labortime_services(self):
        """ Return a list of services use to compute the labor time """
        res = super().get_market_bom_labortime_services()
        product_xmlids = [
            "product_workflow_dec.beq_workforce",
        ]
        for product_xmlid in product_xmlids:
            product_id = self.env.ref(product_xmlid, raise_if_not_found=False)
            if product_id:
                res += product_id
        return res
