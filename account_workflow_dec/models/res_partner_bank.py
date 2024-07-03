# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2025

from odoo import api, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    @api.depends("name", "bank_id")
    def name_get(self):
        """Custom naming to add bank name"""
        super_res = super().name_get()
        res = []
        for item in super_res:
            rec = self.browse(item[0])[0]
            name = item[1]
            if rec.bank_id:
                name = "%s (%s)" % (name, rec.bank_id.display_name)
            res.append((rec.id, name))
        return res or super_res
