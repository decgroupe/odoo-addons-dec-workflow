# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Jan 2021

from odoo import models, api, fields


class ProjectTask(models.Model):
    _inherit = "project.task"

    sequence = fields.Integer(default=0,)

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
