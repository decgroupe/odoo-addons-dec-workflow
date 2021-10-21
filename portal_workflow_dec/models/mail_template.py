# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa@decgroupe.com>, Oct 2021

from odoo import _, api, models


class MailTemplate(models.Model):
    _inherit = "mail.template"

    @api.multi
    def write(self, vals):
        return super().write(vals)
