# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2023

from odoo import api, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.model
    def _get_partner_field_name(self):
        return "partner_shipping_id"
