# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2020

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    amount_untaxed = fields.Monetary(
        string="Total Amount (excluding taxes)",
    )
    amount_total = fields.Monetary(
        string="Total Amount (including taxes)",
    )
    margin = fields.Monetary(
        "Margin (excluding taxes)",
    )

    def copy(self, default=None):
        if self.origin:
            origin = ("%s:%s") % (
                self.origin,
                self.name,
            )
        else:
            origin = self.name

        default = dict(
            default or {},
            origin=origin,
        )
        return super().copy(default)

    def action_quotation_send(self):
        view = super().action_quotation_send()
        # replace default "mail.mail_notification_paynow" layout with an extended one
        # with more variables. (note that this function is called for both rfq/order)
        view["context"][
            "custom_layout"
        ] = "sale_workflow_dec.view_email_template_edi_sale_composer_layout"
        return view
