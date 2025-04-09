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

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        if self._need_auto_tag(vals):
            rec._auto_tag()
        if self._need_auto_activity(vals):
            rec._auto_activity()
        return rec

    def write(self, vals):
        res = super().write(vals)
        if self._need_auto_tag(vals):
            for rec in self:
                rec._auto_tag()
        return res

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
        return vals.get("sale_line_id")

    def _get_auto_tag_data(self):
        self.ensure_one()
        tag_id = False
        origin = False
        if self.sale_line_id:
            # use sudo() to avoid ACL issues
            sale_line_id = self.sudo().sale_line_id
            origin = {
                "res_id": sale_line_id.id,
                "res_model": sale_line_id._name,
            }
            tag_id = self._get_tag_for_product_code(
                sale_line_id.product_id.default_code
            )
        else:
            tag_id = False
        return origin, tag_id

    def _auto_tag(self):
        self.ensure_one()
        # avoid infinite loop
        if self.env.context.get("auto_tag_origin", False):
            return
        origin, tag_id = self._get_auto_tag_data()
        if tag_id:
            self.with_context(auto_tag_origin=origin).write(
                {"tag_ids": [(4, tag_id.id)]},
            )

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
        return vals.get("sale_line_id")

    def _get_auto_activity_data(self):
        self.ensure_one()
        origin = False
        act_values = {}
        if self.sale_line_id:
            # use sudo() to avoid ACL issues
            sale_line_id = self.sudo().sale_line_id
            origin = {
                "res_id": sale_line_id.id,
                "res_model": sale_line_id._name,
            }
            team_id = self._get_team_for_product_code(
                sale_line_id.product_id.default_code
            )
            if team_id:
                act_values = {
                    "team_id": team_id.id,
                    "user_id": team_id.user_id.id,
                }
        return origin, act_values

    def _auto_activity(self):
        self.ensure_one()
        # avoid infinite loop
        if self.env.context.get("auto_activity_origin", False):
            return
        origin, act_values = self._get_auto_activity_data()
        if act_values:
            self.with_context(auto_activity_origin=origin).create_to_assign_activity(
                **act_values,
            )
            self.with_context(auto_activity_origin=origin).create_to_plan_activity(
                **act_values,
            )

    def _compute_show_time_control(self):
        result = super()._compute_show_time_control()
        for rec in self:
            rec.show_time_control = False
        return result
