# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Jun 2021

from odoo import api, fields, models


class ProductPack(models.Model):
    _inherit = 'product.pack.line'

    @api.multi
    def get_sale_order_line_vals(self, line, order):
        vals = super().get_sale_order_line_vals(line, order)
        vals['name'] = vals['name'].replace('> ', '🢖 ')
        return vals
