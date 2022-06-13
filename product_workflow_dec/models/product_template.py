# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jun 2022

from numpy import append
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def action_view_sales_no365(self):
        action = super().action_view_sales()
        if 'domain' in action:
            domain = []
            for field, operator, value in action['domain']:
                # Remove the 365 days limit
                if field == 'date' and operator == '>=':
                    continue
                else:
                    domain.append([field, operator, value])
            action['domain'] = domain
        return action
