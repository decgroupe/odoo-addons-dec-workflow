# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Nov 2020

from odoo import _, api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    def write(self, vals):
        # When linking a contact to a partner, change the adress type to
        # `other`, otherwise existing address will be overriden with the
        # the parent one
        if 'parent_id' in vals and not 'type' in vals:
            vals['type'] = 'other'
        if vals.get('type') == 'private':
            vals['vat'] = False
        return super().write(vals)
