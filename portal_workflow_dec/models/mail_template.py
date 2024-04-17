# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa@decgroupe.com>, Oct 2021

from odoo import _, models


class MailTemplate(models.Model):
    _inherit = "mail.template"
