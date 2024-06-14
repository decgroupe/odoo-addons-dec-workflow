# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jun 2024

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        # like 'odoo/addons/website_sale/models/sale_order.py::SaleOrder.action_confirm'
        # but check if amount_total is set this time
        for order in self:
            if (
                not order.transaction_ids
                and order.amount_total
                and self._context.get("send_email")
            ):
                order._send_order_confirmation_mail()
        return res

