# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2021

from odoo import models, api, fields


class ProjectTask(models.Model):
    _inherit = "project.task"

    sequence = fields.Integer(default=0, )
    display_sale_order = fields.Boolean(compute="_compute_display_sale_order", )

    @api.multi
    def action_open_project_form(self):
        self.ensure_one()
        action = self.env.ref('project.open_view_project_all').read()[0]
        action['res_id'] = self.project_id.id
        action['view_mode'] = 'form'
        view = self.env.ref("project.edit_project", False)
        action["views"] = [(view and view.id or False, "form")]
        action['context'] = {}
        # Replace main with current to avoid clearing breadcrumb
        action['target'] = 'current'
        return action

    @api.multi
    @api.depends('sale_order_id', 'project_id')
    def _compute_display_sale_order(self):
        for rec in self:
            rec.display_sale_order = False
            if rec.sale_order_id and rec.sale_order_id.name != rec.project_id.name:
                rec.display_sale_order = True
