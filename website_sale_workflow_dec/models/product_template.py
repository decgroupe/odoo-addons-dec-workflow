# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Nov 2020

from odoo import models, fields
from odoo.tools import html_translate


class ProductTemplate(models.Model):
    _inherit = "product.template"

    website_head_description = fields.Html(
        sanitize_attributes=False, translate=html_translate
    )

    website_image_description = fields.Html(
        sanitize_attributes=False, translate=html_translate
    )
