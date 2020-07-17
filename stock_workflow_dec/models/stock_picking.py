# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, July 2020

from odoo import models, api, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"
    _order = "id desc"
