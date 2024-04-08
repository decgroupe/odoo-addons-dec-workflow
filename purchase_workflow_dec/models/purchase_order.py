# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _order = "id desc"

    def action_rfq_send(self):
        view = super().action_rfq_send()
        # replace default "mail.mail_notification_paynow" layout with an extended one
        # with more variables. (note that this function is called for both rfq/order)
        view["context"][
            "custom_layout"
        ] = "purchase_workflow_dec.view_email_template_edi_purchase_composer_layout"
        return view
