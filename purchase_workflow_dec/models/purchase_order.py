# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _order = "id desc"

    @api.model
    def create(self, vals):
        # set name from sequence before built-in purchase.create to use the current
        # date as reference
        company_id = vals.get(
            "company_id", self.default_get(["company_id"])["company_id"]
        )
        self_comp = self.with_company(company_id)
        if vals.get("name", "New") == "New":
            seq_date = fields.Datetime.now()
            vals["name"] = (
                self_comp.env["ir.sequence"].next_by_code(
                    "purchase.order", sequence_date=seq_date
                )
                or "/"
            )
        res = super(PurchaseOrder, self_comp).create(vals)
        return res

    def action_rfq_send(self):
        view = super().action_rfq_send()
        # replace default "mail.mail_notification_paynow" layout with an extended one
        # with more variables. (note that this function is called for both rfq/order)
        view["context"][
            "custom_layout"
        ] = "purchase_workflow_dec.view_email_template_edi_purchase_composer_layout"
        return view
