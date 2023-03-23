# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2021

from odoo import _, models, api, fields

DO_DIGITAL_PREFIX = "BNU_"
DO_EQUIPMENT_PREFIX = "BEQ_"

class ProjectTask(models.Model):
    _inherit = "project.task"

    sequence = fields.Integer(default=0, )
    display_sale_order = fields.Boolean(compute="_compute_display_sale_order", )

    @api.multi
    @api.depends('sale_order_id', 'project_id')
    def _compute_display_sale_order(self):
        for rec in self:
            rec.display_sale_order = False
            if rec.sale_order_id and rec.sale_order_id.name != rec.project_id.name:
                rec.display_sale_order = True

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        if vals and vals.get('sale_line_id'):
            rec._auto_tag_from_sale()
            rec._auto_activity_from_sale()
        return rec

    @api.multi
    def write(self, vals):
        res = super().write(vals)
        if vals.get('sale_line_id'):
            for rec in self:
                rec._auto_tag_from_sale()
        return res

    def _auto_tag_from_sale(self):
        self.ensure_one()
        if self.sale_line_id:
            code = self.sale_line_id.product_id.default_code
            if code.startswith(DO_DIGITAL_PREFIX):
                self._tag_with(
                    "project_workflow_dec.project_tag_design_office_digital"
                )
            elif code.startswith(DO_EQUIPMENT_PREFIX):
                self._tag_with(
                    "project_workflow_dec.project_tag_design_office_equipment"
                )

    def _tag_with(self, tag_ref):
        tag = self.env.ref(tag_ref)
        if tag:
            self.write({'tag_ids': [(4, tag.id)]})

    def _auto_activity_from_sale(self):
        self.ensure_one()
        if self.sale_line_id:
            code = self.sale_line_id.product_id.default_code
            if code.startswith(DO_DIGITAL_PREFIX):
                self._activity_todo_for(
                    "mail_activity_workflow_dec.team_design_office_digital"
                )
            elif code.startswith(DO_EQUIPMENT_PREFIX):
                self._activity_todo_for(
                    "mail_activity_workflow_dec.team_design_office_equipment"
                )

    def _activity_todo_for(self, team_ref):
        self.ensure_one()
        team_id = self.env.ref(team_ref)
        if team_id:
            self.with_context(
                mail_activity_noautofollow=True,
            ).activity_schedule(
                act_type_xmlid='mail.mail_activity_data_todo',
                note=_("🚨 Auto: To Assign and to Plan"),
                user_id=team_id.user_id.id,
                team_id=team_id.id
            )

    def _compute_show_time_control(self):
        result = super()._compute_show_time_control()
        for rec in self:
            rec.show_time_control = False
        return result
