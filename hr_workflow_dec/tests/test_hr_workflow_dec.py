# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Oct 2023

from odoo.addons.hr_expense.tests.common import TestExpenseCommon
from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.tests import tagged


@tagged("-at_install", "post_install")
class TestHrWorkflowDec(TestExpenseCommon):
    def setUp(self):
        super().setUp()
        self.sheet_model = self.env["hr.expense.sheet"]

    def test_01_manager(self):
        self.assertFalse(
            self.expense_employee.expense_manager_id,
            "Expense manager should not be set for this employee",
        )
        # create a new expense sheet
        sheet1_id = self.sheet_model.create({"employee_id": self.expense_employee.id})
        self.assertFalse(
            sheet1_id.user_id, "Expense manager should not be set for this sheet"
        )
        # override default manager
        ICP = self.env["ir.config_parameter"].sudo()
        ICP.set_param("hr_workflow_dec.default_user_id", self.expense_user_manager.id)
        # create a new expense sheet
        sheet2_id = self.sheet_model.create({"employee_id": self.expense_employee.id})
        self.assertEqual(
            sheet2_id.user_id,
            self.expense_user_manager,
            "Expense manager should be set",
        )
        # set an alternative expense manager for this user
        alt_expense_user_manager = mail_new_test_user(
            self.env,
            name="Expense manager",
            login="expense_manager_2",
            email="expense_manager_2@example.com",
            notification_type="email",
            groups="base.group_user,hr_expense.group_hr_expense_manager",
            company_ids=[(6, 0, self.env.companies.ids)],
        )
        self.expense_employee.expense_manager_id = alt_expense_user_manager
        # create a new expense sheet
        sheet3_id = self.sheet_model.create({"employee_id": self.expense_employee.id})
        self.assertEqual(
            sheet3_id.user_id,
            alt_expense_user_manager,
            "Alternative expense manager should be set",
        )
