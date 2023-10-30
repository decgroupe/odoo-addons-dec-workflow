# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Dec 2021

from odoo import api, fields, models


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    # Redefine default using lambda because the default implementation use direct
    # function string and is not inheritable
    journal_id = fields.Many2one(
        default=lambda self: self._default_journal_id(),
    )

    @api.model
    def create(self, vals):
        # Disable subscribe notify for expense sheet on create
        rec = super(
            HrExpenseSheet, self.with_context(mail_auto_subscribe_no_notify=True)
        ).create(vals)
        return rec

    @api.depends("employee_id")
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

    @api.model
    def _default_journal_id(self):
        # Restore 12.0 code to get default journal for expense (Journal des OD)
        journal = self.env.ref(
            "hr_expense.hr_expense_account_journal", raise_if_not_found=False
        )
        if not journal or journal.sudo().company_id not in self.env.companies:
            return super()._default_journal_id()
        return journal.id
