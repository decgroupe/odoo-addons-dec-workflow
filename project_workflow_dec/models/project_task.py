# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2021

from odoo import models, api, fields


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
            if code.startswith('BNU_'):
                self._tag_with(
                    "project_workflow_dec.project_tag_design_office_digital"
                )
            elif code.startswith('BEQ_'):
                self._tag_with(
                    "project_workflow_dec.project_tag_design_office_equipment"
                )

    def _tag_with(self, tag_ref):
        tag = self.env.ref(tag_ref)
        if tag:
            self.write({'tag_ids': [(4, tag.id)]})


    def _compute_show_time_control(self):
        result = super()._compute_show_time_control()
        for rec in self:
            rec.show_time_control = False
        return result
