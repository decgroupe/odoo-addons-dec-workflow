# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025

from odoo.tests.common import TransactionCase


class TestProjectWorkflowDec(TransactionCase):

    def _create_so(self, partner_id):
        return (
            self.env["sale.order"]
            .with_context(
                mail_notrack=True,
                mail_create_nolog=True,
            )
            .create(
                {
                    "partner_id": partner_id.id,
                    "partner_invoice_id": partner_id.id,
                    "partner_shipping_id": partner_id.id,
                }
            )
        )

    def _create_so_line(self, sale_order_id, product_id, product_uom_qty=1):
        return self.env["sale.order.line"].create(
            {
                "order_id": sale_order_id.id,
                "name": product_id.name,
                "product_id": product_id.id,
                "product_uom_qty": product_uom_qty,
                "product_uom": product_id.uom_id.id,
                "price_unit": product_id.list_price,
            }
        )

    def setUp(self):
        super().setUp()
        # tags
        self.tag_equipment = self.env.ref(
            "project_workflow_dec.project_tag_design_office_equipment"
        )
        self.tag_digital = self.env.ref(
            "project_workflow_dec.project_tag_design_office_digital"
        )
        # products
        self.service_bnu_sdd = self.env.ref("project_workflow_dec.service_bnu_sdd")
        self.service_bnu_ost = self.env.ref("project_workflow_dec.service_bnu_ost")
        self.service_beq_sdd = self.env.ref("project_workflow_dec.service_beq_sdd")
        self.service_beq_adooi = self.env.ref("project_workflow_dec.service_beq_adooi")
        # reference to another service: Senior Architect (Invoice on Timesheets)
        self.service_senior_architect = self.env.ref(
            "sale_timesheet.product_service_deliver_timesheet_1"
        )
        # activity types
        self.activity_to_assign = self.env.ref(
            "project_activity.mail_activity_to_assign"
        )
        self.activity_to_plan = self.env.ref("project_activity.mail_activity_to_plan")
        # ensure tags are present
        self.assertIsNotNone(self.tag_equipment, "Tag Equipment not found")
        self.assertIsNotNone(self.tag_digital, "Tag Digital not found")
        # users
        self.user_jd = self.env.ref("project_workflow_dec.user_jd")
        # stages
        self.task_stage_new = self.env.ref("project.project_stage_0")
        self.task_stage_done = self.env.ref("project.project_stage_2")
        self.task_stage_cancelled = self.env.ref("project.project_stage_3")

    def test_10_no_auto_activity(self):
        # create a task out of any workflow
        task_id = self.env["project.task"].create(
            {
                "name": "Test task",
                "project_id": self.env.ref("project.project_project_1").id,
                "user_id": self.env.ref("base.user_admin").id,
            }
        )
        self.assertFalse(task_id.tag_ids, "Task should not be tagged")
        self.assertFalse(task_id.activity_ids, "Task should not have any activity")

    def _create_so_with_3_lines(self):
        # create a sale order for Azure Interior
        order_id = self._create_so(self.env.ref("base.res_partner_12"))
        # create a 1st sale order line for the service "On-site training"
        sol1_id = self._create_so_line(order_id, self.service_bnu_ost, 2)
        # create a 2nd sale order line for the service "Specific design/development"
        sol2_id = self._create_so_line(order_id, self.service_beq_sdd, 1)
        # create a 3rd sale order line for another service
        sol3_id = self._create_so_line(order_id, self.service_senior_architect, 1)
        # sale confirmation
        order_id.action_confirm()
        # ensure three tasks are created
        self.assertEqual(len(order_id.tasks_ids), 3, "Three tasks should be created")
        self.assertEqual(
            set(order_id.tasks_ids.mapped("sale_line_id")),
            set([sol1_id, sol2_id, sol3_id]),
            "Tasks sale lines should match the sale order lines",
        )
        return order_id, sol1_id, sol2_id, sol3_id

    def test_20_auto_tag(self):
        order_id, sol1_id, sol2_id, sol3_id = self._create_so_with_3_lines()
        self.assertIn(
            self.tag_digital, sol1_id.task_id.tag_ids, "Task should be tagged"
        )
        self.assertIn(
            self.tag_equipment, sol2_id.task_id.tag_ids, "Task should be tagged"
        )
        self.assertFalse(sol3_id.task_id.tag_ids, "Task should not be tagged")

    def test_30_auto_activity(self):
        order_id, sol1_id, sol2_id, sol3_id = self._create_so_with_3_lines()
        # check that the tasks have activities
        sol_ids = sol1_id | sol2_id | sol3_id
        for sol_id in [sol1_id, sol2_id]:
            self.assertEqual(
                len(sol_id.task_id.activity_ids), 2, "Task should have two activities"
            )
        self.assertFalse(sol3_id.task_id.activity_ids, "Task should have no activities")

        # check that the activities are of the right type
        activity_types = (
            sol_ids.mapped("task_id").mapped("activity_ids").mapped("activity_type_id")
        )
        self.assertIn(self.activity_to_assign, activity_types)
        self.assertIn(self.activity_to_plan, activity_types)
        # test "assign to me"
        sol1_id.task_id.with_user(self.user_jd).action_assign_to_me()
        # check that the task is correctly assigned
        # and that the activity has been dropped
        self.assertEqual(sol1_id.task_id.user_id, self.user_jd)
        self.assertEqual(
            len(sol1_id.task_id.activity_ids), 1, "Task should have one activity"
        )
        # set the task to "done"
        sol1_id.task_id.write({"stage_id": self.task_stage_done.id})
        self.assertFalse(sol1_id.task_id.activity_ids, "Task should have no activities")
        # create a new sale order line that will immediatly create a task
        sol4_id = self._create_so_line(order_id, self.service_beq_adooi, 1)
        task4_id = sol4_id.task_id
        self.assertEqual(
            len(task4_id.activity_ids), 2, "Task should have two activities"
        )
        # set the task to "cancelled" and remove that link with the sale order line
        task4_id.write(
            {
                "stage_id": self.task_stage_cancelled.id,
                "sale_line_id": False,
            }
        )
        self.assertFalse(task4_id.activity_ids, "Task should have no activities")
        # reset this task to "draft" and assign it ti the same sale order line
        task4_id.write(
            {
                "stage_id": self.task_stage_new.id,
                "sale_line_id": sol4_id.id,
            }
        )
        # ensure no activities are re-created
        self.assertFalse(task4_id.activity_ids, "Task should still have no activities")



    def test_40_(self):
        pass
        #TODO: set date_deadline
        #TODO: set check assigned team

