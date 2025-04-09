# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025

import datetime
from odoo import fields
from .common import TestProjectWorkflowDecCommon


class TestProjectWorkflowDec(TestProjectWorkflowDecCommon):

    def setUp(self):
        super().setUp()

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
        for sol_id in sol_ids:
            self.assertEqual(
                len(sol_id.task_id.activity_ids), 2, "Task should have two activities"
            )
        # check that the activities are of the right type
        activity_types = (
            sol_ids.mapped("task_id").mapped("activity_ids").mapped("activity_type_id")
        )
        self.assertIn(self.activity_to_assign, activity_types)
        self.assertIn(self.activity_to_plan, activity_types)
        # test "assign to me"
        sol1_id.task_id.with_user(self.bnu_user_jd).action_assign_to_me()
        # check that the task is correctly assigned
        # and that the activity has been dropped
        self.assertEqual(sol1_id.task_id.user_id, self.bnu_user_jd)
        self.assertEqual(
            len(sol1_id.task_id.activity_ids),
            1,
            "Task should now have only one activity",
        )
        # remaining activity should be "to plan"
        self.assertIn(
            self.activity_to_plan, sol1_id.task_id.activity_ids.activity_type_id
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
        # test set "date_deadline" to tomorrow
        sol2_id.task_id.with_user(self.beq_user_mw).date_deadline = (
            fields.date.today() + datetime.timedelta(days=1)
        )
        self.assertEqual(
            len(sol2_id.task_id.activity_ids),
            1,
            "Task should now have only one activity",
        )
        # remaining activity should be "to assign"
        self.assertIn(
            self.activity_to_assign, sol2_id.task_id.activity_ids.activity_type_id
        )

    def test_40_check_assigned_team(self):
        _order_id, sol1_id, sol2_id, sol3_id = self._create_so_with_3_lines()
        team1_ids = sol1_id.task_id.activity_ids.mapped("team_id")
        user1_ids = sol1_id.task_id.activity_ids.mapped("user_id")
        self.assertEqual(team1_ids, self.team_design_office_digital)
        self.assertFalse(user1_ids)
        team2_ids = sol2_id.task_id.activity_ids.mapped("team_id")
        user2_ids = sol2_id.task_id.activity_ids.mapped("user_id")
        self.assertEqual(team2_ids, self.team_design_office_equipment)
        self.assertFalse(user2_ids)
        team3_ids = sol3_id.task_id.activity_ids.mapped("team_id")
        user3_ids = sol3_id.task_id.activity_ids.mapped("user_id")
        self.assertFalse(team3_ids)
        self.assertEqual(user3_ids, self.env.user)
