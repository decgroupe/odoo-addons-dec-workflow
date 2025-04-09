# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2025

from odoo.tests.common import TransactionCase


class TestProjectWorkflowDecCommon(TransactionCase):

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
        # teams
        self.team_design_office_digital = self.env.ref(
            "mail_activity_workflow_dec.team_design_office_digital"
        )
        self.team_design_office_equipment = self.env.ref(
            "mail_activity_workflow_dec.team_design_office_equipment"
        )
        self.team_support_functions = self.env.ref(
            "mail_activity_workflow_dec.team_support_functions"
        )
        self.team_treading = self.env.ref("mail_activity_workflow_dec.team_trading")
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
        self.bnu_user_jd = self.env.ref("project_workflow_dec.user_jd")
        self.beq_user_mw = self.env.ref("project_workflow_dec.user_mw")
        # stages
        self.task_stage_new = self.env.ref("project.project_stage_0")
        self.task_stage_done = self.env.ref("project.project_stage_2")
        self.task_stage_cancelled = self.env.ref("project.project_stage_3")
