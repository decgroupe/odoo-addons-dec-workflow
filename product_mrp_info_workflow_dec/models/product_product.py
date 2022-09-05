# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Sep 2022

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def action_view_mrp_productions(self):
        """ Override `action_view_mrp_productions` from `product_mrp_info`
            to use the kanban view from `mrp_stage`
        """
        super().action_view_mrp_productions()
        product_ids = self.ids
        return self.env['mrp.production'].action_view_staged(product_ids)
