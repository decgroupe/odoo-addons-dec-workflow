# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Override default report with aeroo one

    def print_quotation(self):
        super().print_quotation()
        return (
            self.env.ref("sale_report_aeroo.sale_order_report")
            .with_context(discard_logo_check=True)
            .report_action(self)
        )
