# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025


from odoo.tests import Form
from odoo.addons.project_workflow_dec.tests.common import TestProjectWorkflowDecCommon


class TestMrpProjectWorkflowDec(TestProjectWorkflowDecCommon):

    def _generate_mo(self, product, bom, qty=1.0):
        mo_form = Form(self.env["mrp.production"])
        mo_form.product_id = product
        mo_form.bom_id = bom
        mo_form.product_qty = qty
        mo = mo_form.save()
        return mo

    def setUp(self):
        super().setUp()
        # [FURN_7800] Desk Combination
        self.desk_product_id = self.env.ref("product.product_product_3")
        # BoM for [FURN_7800] Desk Combination
        self.desk_bom_id = self.env.ref("mrp.mrp_bom_manufacture")
        self.assertIn(self.desk_bom_id, self.desk_product_id.bom_ids)

    def test_10_no_auto_activity(self):
        # create a task out of any workflow (to increase coverage)
        task_id = self.env["project.task"].create(
            {
                "name": "Test task",
                "project_id": self.env.ref("project.project_project_1").id,
                "user_id": self.env.ref("base.user_admin").id,
            }
        )
        self.assertFalse(task_id.tag_ids, "Task should not be tagged")
        self.assertFalse(task_id.activity_ids, "Task should not have any activity")

    def test_20_bom_with_service(self):
        # add [BNU_OST] On-site training to the BOM
        self.env["mrp.bom.line"].create(
            {
                "bom_id": self.desk_bom_id.id,
                "product_id": self.service_bnu_ost.id,
                "product_qty": 1,
            }
        )
        self.assertEqual(len(self.desk_bom_id.bom_line_ids), 4)
        # generate a MO
        desk_mo1_id = self._generate_mo(self.desk_product_id, self.desk_bom_id)
        desk_mo1_id.action_confirm()
        self.assertEqual(desk_mo1_id.state, "confirmed")
        # check that the task has been created
        self.assertEqual(len(desk_mo1_id.task_ids), 1, "One task should be created")
        # check that the task has been tagged
        self.assertIn(
            self.tag_digital, desk_mo1_id.task_ids.tag_ids, "Task should be tagged"
        )
        # check that the task has both activities
        self.assertEqual(len(desk_mo1_id.task_ids.activity_ids), 2)
        # check that the activities are of the right type
        activity_types = desk_mo1_id.task_ids.mapped("activity_ids").mapped(
            "activity_type_id"
        )
        self.assertIn(self.activity_to_assign, activity_types)
        self.assertIn(self.activity_to_plan, activity_types)
