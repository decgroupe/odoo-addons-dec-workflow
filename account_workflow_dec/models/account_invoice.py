# Copyright (C) DEC SARL, Inc - All Rights Reserved.
#
# CONFIDENTIAL NOTICE: Unauthorized copying and/or use of this file,
# via any medium is strictly prohibited.
# All information contained herein is, and remains the property of
# DEC SARL and its suppliers, if any.
# The intellectual and technical concepts contained herein are
# proprietary to DEC SARL and its suppliers and may be covered by
# French Law and Foreign Patents, patents in process, and are
# protected by trade secret or copyright law.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from DEC SARL.
# Written by Yann Papouin <y.papouin@dec-industrie.com>, May 2020

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.depends('origin')
    def _compute_client_order_ref(self):
        SaleOrder = self.env['sale.order']
        for invoice in self:
            res = []
            if invoice.origin:
                res.append(invoice.origin)
                for order in SaleOrder.search([('name', '=', invoice.origin)]):
                    if order.client_order_ref:
                        res.append(order.client_order_ref)
                invoice.client_order_ref = ' '.join(res)
            else:
                invoice.client_order_ref = False

    # Legacy field used to get the client reference stored in the sale order.
    # Note that this value should be accessible from 'reference' or 'name'
    # field now
    client_order_ref = fields.Char(
        string='Customer Reference',
        compute='_compute_client_order_ref',
        readonly=True,
    )

    # This field is only used to match the old procedure where the invoice is
    # set by a stamp on the paper stored in a cabinet, so the ERP must keep a
    # trace for this value
    company_invoice_number = fields.Char(
        'Company invoice number',
        size=64,
        readonly=False,
        states={'draft': [('readonly', False)]}
    )
