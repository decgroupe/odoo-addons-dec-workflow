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
# Written by Yann Papouin <y.papouin@dec-industrie.com>, Mar 2020

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    # def _get_validity_date(self):
    #     for order in self:
    #         order.validity_date  = order.date_order + relativedelta(days=order.validity or 0.0)

    summary = fields.Char(
        size=128,
        help="Order summary to quickly identify this order in treeview",
    )
    # validity = fields.Integer(
    #     'Validity period',
    #     readonly=True,
    #     states={'draft': [('readonly', False)]},
    #     help="Validity delay in day(s)"
    # )
    warranty = fields.Integer(
        'Warranty period',
        readonly=True,
        states={'draft': [('readonly', False)]},
        help="Warranty delay in year(s)",
        default=2
    )
    # validity_date = fields.Date(
    #     compute=_get_validity_date,
    #     store=True,
    #     help="Date of validity"
    # )

    partner_shipping_zip_id = fields.Many2one(
        'res.city.zip',
        'ZIP Location',
        related='partner_shipping_id.zip_id',
        readonly=True,
    )
