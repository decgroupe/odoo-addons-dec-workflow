# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # Override default report with aeroo one

    def print_quotation(self):
        super().print_quotation()
        return self.env.ref(
            "purchase_report_aeroo.purchase_order_report"
        ).report_action(self)
