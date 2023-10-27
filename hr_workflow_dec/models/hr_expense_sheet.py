# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Dec 2021

from odoo import api, models


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    @api.model
    def create(self, vals):
        # Disable subscribe notify for expense sheet on create
        rec = super(
            HrExpenseSheet, self.with_context(mail_auto_subscribe_no_notify=True)
        ).create(vals)
        return rec

    @api.depends('employee_id')
    def _compute_from_employee_id(self):
        super()._compute_from_employee_id()
        ICP = self.env["ir.config_parameter"].sudo()
        default_user_id = ICP.get_param("hr_workflow_dec.default_user_id")
        if default_user_id:
            default_user_id = self.env["res.users"].search(
                [("id", "=", default_user_id)], limit=1
            )
            if default_user_id:
                for sheet in self:
                    # only override manager if no one is set for this employee
                    if not sheet.user_id or not sheet.employee_id.expense_manager_id:
                        sheet.user_id = default_user_id
