# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2022

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_view_project_ids(self):
        """ In default behaviour a kanban view is returned even if there is
            only one project (unbillable but with billable tasks). Our
            override search for these billable tasks and return the project
            overview only if one project exsits.
        """
        self.ensure_one()
        unbillable_project_ids = self.project_ids.filtered(
            lambda project: not project.sale_line_id
        )
        billable_task_ids = unbillable_project_ids.mapped('task_ids').filtered(
            lambda task: task.sale_line_id
        )
        billable_project_ids = billable_task_ids.mapped('project_id')

        if len(billable_project_ids
              ) == 1 and billable_task_ids and self.env.user.has_group(
                  'project.group_project_manager'
              ):
            return billable_task_ids[0].project_id.action_view_timesheet_plan()
        else:
            return super().action_view_project_ids()
