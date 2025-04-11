# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Oct 2023

from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.tests.common import TransactionCase


class TestHrWorkflowDec2(TransactionCase):
    def setUp(self):
        super().setUp()
        self.sheet_model = self.env["hr.expense.sheet"]
        # Recreate employee data like .odoo/addons/hr_expense/tests/common.py
        self.basic_expense_user = mail_new_test_user(
            self.env,
            name="basic_expense_user",
            login="basic_expense_user",
            email="basic_expense_user@example.com",
            notification_type="email",
            groups="base.group_user",
            company_ids=[(6, 0, self.env.companies.ids)],
        )
        self.basic_expense_employee = self.env["hr.employee"].create(
            {
                "name": "expense_employee",
                "user_id": self.basic_expense_user.id,
                "address_home_id": self.basic_expense_user.partner_id.id,
                "address_id": self.basic_expense_user.partner_id.id,
            }
        )

    def test_01_default_journal(self):
        # create a new expense sheet
        sheet1_id = self.sheet_model.create(
            {"employee_id": self.basic_expense_employee.id}
        )
        self.assertEqual(
            sheet1_id.journal_id,
            self.env.ref("hr_workflow_dec.od_journal"),
            "Default journal should be specific",
        )
