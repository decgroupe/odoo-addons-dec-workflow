# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    # This field is only used to match the old procedure where the invoice is
    # set by a stamp on the paper stored in a cabinet, so the ERP must keep a
    # trace for this value
    company_invoice_number = fields.Char(
        string="Company invoice number",
        size=64,
        readonly=False,
        states={"draft": [("readonly", False)]},
    )
    amount_untaxed = fields.Monetary(
        string="Total Amount (excluding taxes)",
    )
    amount_tax = fields.Monetary(
        string="Taxes",
    )
    amount_total = fields.Monetary(
        string="Total Amount (including taxes)",
    )
    amount_residual = fields.Monetary(
        string="Amount Due (including taxes)",
    )
    amount_untaxed_signed = fields.Monetary(
        string="Total Amount (excluding taxes) ±",
    )
    amount_tax_signed = fields.Monetary(
        string="Taxes ±",
    )
    amount_total_signed = fields.Monetary(
        string="Total Amount (including taxes) ±",
    )
    amount_residual_signed = fields.Monetary(
        string="Amount Due (including taxes) ±",
    )

    @api.model
    def create(self, vals):
        # Disable subscribe notify for invoices on create
        invoice = super(
            AccountMove, self.with_context(mail_auto_subscribe_no_notify=True)
        ).create(vals)
        return invoice
