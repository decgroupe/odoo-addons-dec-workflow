# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa@decgroupe.com>, Apr 2024

from odoo import _, api, models, fields


class Company(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    portal_name = fields.Char(
        string="Portal Name",
        compute="_compute_portal_name",
    )

    @api.depends("name")
    def _compute_portal_name(self):
        for rec in self:
            rec.portal_name = _("%s's Portal") % (rec.name)

