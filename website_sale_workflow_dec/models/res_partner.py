# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2022

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    website_show_price = fields.Boolean(default=False)
