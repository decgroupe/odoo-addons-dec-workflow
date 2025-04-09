# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2021

from odoo import _, api, fields, models

DO_DIGITAL_PREFIX = "BNU_"
DO_EQUIPMENT_PREFIX = "BEQ_"


class ProjectTask(models.Model):
    _inherit = "project.task"

    sequence = fields.Integer(
        default=0,
    )
    display_sale_order = fields.Boolean(
        compute="_compute_display_sale_order",
    )

    @api.depends("sale_order_id", "project_id")
    def _compute_display_sale_order(self):
        for rec in self:
            rec.display_sale_order = False
            if rec.sale_order_id and rec.sale_order_id.name != rec.project_id.name:
                rec.display_sale_order = True

    def _get_tag_for_product_code(self, product_code):
        self.ensure_one()
        if product_code and product_code.startswith(DO_DIGITAL_PREFIX):
            return self.env.ref(
                "project_workflow_dec.project_tag_design_office_digital"
            )
        elif product_code and product_code.startswith(DO_EQUIPMENT_PREFIX):
            return self.env.ref(
                "project_workflow_dec.project_tag_design_office_equipment"
            )
        else:
            return False

    @api.model
    def _need_auto_tag(self, vals):
        return super()._need_auto_tag(vals) or vals.get("sale_line_id")

    def _get_auto_tag_data(self):
        self.ensure_one()
        origin, tag_id = super()._get_auto_tag_data()
        if self.sale_line_id:
            # use sudo() to avoid ACL issues
            sale_line_id = self.sudo().sale_line_id
            origin.update({
                "res_id": sale_line_id.id,
                "res_model": sale_line_id._name,
            })
            tag_id = self._get_tag_for_product_code(
                sale_line_id.product_id.default_code
            )
        else:
            tag_id = False
        return origin, tag_id

    def _get_team_for_product_code(self, product_code):
        self.ensure_one()
        if product_code and product_code.startswith(DO_DIGITAL_PREFIX):
            return self.env.ref("mail_activity_workflow_dec.team_design_office_digital")
        elif product_code and product_code.startswith(DO_EQUIPMENT_PREFIX):
            return self.env.ref(
                "mail_activity_workflow_dec.team_design_office_equipment"
            )
        else:
            return False

    @api.model
    def _need_auto_activity(self, vals):
        return super()._need_auto_activity(vals) or vals.get("sale_line_id")

    def _get_auto_activity_data(self):
        self.ensure_one()
        origin, act_values = super()._get_auto_activity_data()
        if self.sale_line_id:
            # use sudo() to avoid ACL issues
            sale_line_id = self.sudo().sale_line_id
            origin.update(
                {
                    "res_id": sale_line_id.id,
                    "res_model": sale_line_id._name,
                }
            )
            team_id = self._get_team_for_product_code(
                sale_line_id.product_id.default_code
            )
            if team_id:
                act_values.update(
                    {
                        "team_id": team_id.id,
                        "user_id": team_id.user_id.id,
                    }
                )
        return origin, act_values

    def _compute_show_time_control(self):
        result = super()._compute_show_time_control()
        for rec in self:
            rec.show_time_control = False
        return result
