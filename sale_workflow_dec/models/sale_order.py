# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2020

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_image_small = fields.Binary(
        related='partner_id.image_small',
        string='Partner Logo',
    )
    user_image_small = fields.Binary(
        related='user_id.image_small',
        string='User Avatar',
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
