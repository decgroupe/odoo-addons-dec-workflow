# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025

from odoo import _, api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def _need_auto_tag(self, vals):
        return super()._need_auto_tag(vals) or vals.get("bom_line_id")

    def _get_auto_tag_data(self):
        tag_id = super()._get_auto_tag_data()
        if not tag_id and self.bom_line_id:
            # use sudo() to avoid ACL issues
            tag_id = self._get_tag_for_product_code(
                self.sudo().bom_line_id.product_id.default_code
            )
        return tag_id

    @api.model
    def _need_auto_activity(self, vals):
        return super()._need_auto_activity(vals) or vals.get("bom_line_id")

    def _get_auto_activity_data(self):
        origin, team_id = super()._get_auto_activity_data()
        if not team_id and self.bom_line_id:
            origin = self.bom_line_id
            # use sudo() to avoid ACL issues
            team_id = self._get_team_for_product_code(
                self.sudo().bom_line_id.product_id.default_code
            )
        return origin, team_id
