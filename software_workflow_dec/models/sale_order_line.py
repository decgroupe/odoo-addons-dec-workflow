# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2023

from odoo import _, api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _create_application_pass(self):
        pass_id = super()._create_application_pass()
        digital_team_id = self.env.ref(
            "mail_activity_workflow_dec.team_design_office_digital"
        )
        if digital_team_id:
            pass_id.with_context(
                mail_activity_noautofollow=True,
            ).activity_schedule(
                act_type_xmlid='mail.mail_activity_data_todo',
                note=_("🚨 Auto: To Send"),
                user_id=digital_team_id.user_id.id,
                team_id=digital_team_id.id
            )
        return pass_id
