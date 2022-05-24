# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Nov 2020

from odoo import _, api, models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model_create_multi
    def create(self, vals):
        records = super().create(vals)
        records._clear_vat()
        return records

    def write(self, vals):
        # When linking a contact to a partner, change the adress type to
        # `other`, otherwise existing address will be overriden with the
        # the parent one
        if 'parent_id' in vals and not 'type' in vals:
            vals['type'] = 'other'
        if vals.get('type') == 'private':
            vals['vat'] = False
        res = super().write(vals)
        self._clear_vat()
        return res

    def _clear_vat(self):
        if not self.env.context.get('clearing_vat'):
            private_partners = self.filtered('vat').filtered(
                lambda rec: rec.type == 'private'
            )
            private_partners.with_context(clearing_vat=True).write(
                {'vat': False}
            )
