# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Dec 2021

from odoo import api, fields, models, _


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        super()._onchange_employee_id()
        ICP = self.env['ir.config_parameter'].sudo()
        default_user_id = ICP.get_param('hr_workflow_dec.default_user_id')
        if default_user_id:
            default_user_id = self.env['res.users'].search(
                [('id', '=', default_user_id)], limit=1
            )
            if default_user_id:
                self.user_id = default_user_id
