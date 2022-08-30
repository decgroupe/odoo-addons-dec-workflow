# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Aug 2022

from odoo import api, models, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def _get_partner_field_name(self):
        return 'partner_shipping_id'
