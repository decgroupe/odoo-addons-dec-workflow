# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, May 2020

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _order = "id desc"

    partner_image_small = fields.Binary(
        related='partner_id.image_small',
        string='Supplier Logo',
    )
