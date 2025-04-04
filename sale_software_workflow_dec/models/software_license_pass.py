# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025

from odoo import _, api, fields, models


class SoftwareLicensePass(models.Model):
    _inherit = "software.license.pass"

    def _override_to_send_activity_values(self, origin, act_values):
        super()._override_to_send_activity_values(origin=origin, act_values=act_values)
        digital_team_id = self.env.ref(
            "mail_activity_workflow_dec.team_design_office_digital"
        )
        act_values.update(
            {
                "user_id": digital_team_id.user_id.id,
                "team_id": digital_team_id.id,
            }
        )
