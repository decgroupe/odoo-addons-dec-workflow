# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025

from odoo import _, api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def _need_auto_tag(self, vals):
        return super()._need_auto_tag(vals) or vals.get("bom_line_id")

    def _get_auto_tag_data(self):
        origin, tag_id = super()._get_auto_tag_data()
        if self.bom_line_id:
            # use sudo() to avoid ACL issues
            bom_line_id = self.sudo().bom_line_id
            origin.update({
                "res_id": bom_line_id.id,
                "res_model": bom_line_id._name,
            })
            # use sudo() to avoid ACL issues
            tag_id = self._get_tag_for_product_code(
                bom_line_id.product_id.default_code
            )
        else:
            tag_id = False
        return origin, tag_id

    @api.model
    def _need_auto_activity(self, vals):
        return super()._need_auto_activity(vals) or vals.get("bom_line_id")

    def _get_auto_activity_data(self):
        origin, act_values = super()._get_auto_activity_data()
        if self.bom_line_id:
            # use sudo() to avoid ACL issues
            bom_line_id = self.sudo().bom_line_id
            origin.update(
                {
                    "res_id": bom_line_id.id,
                    "res_model": bom_line_id._name,
                }
            )
            team_id = self._get_team_for_product_code(
                bom_line_id.product_id.default_code
            )
            if team_id:
                act_values.update(
                    {
                        "team_id": team_id.id,
                        "user_id": team_id.user_id.id,
                    }
                )
        return origin, act_values
