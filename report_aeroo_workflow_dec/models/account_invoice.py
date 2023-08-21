# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2020

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    # Override default report with aeroo one

    def invoice_print(self):
        """Print the invoice and mark it as sent, so that we can see more
        easily the next step of the workflow
        """
        super().invoice_print()
        if self.user_has_groups("account.group_account_invoice"):
            return (
                self.env.ref("account_report_aeroo.account_invoice_report")
                .with_context(discard_logo_check=True)
                .report_action(self)
            )
        else:
            # FIXME: This report does not exists actually
            return (
                self.env.ref(
                    "account_report_aeroo.account_invoice_without_payment_report"
                )
                .with_context(discard_logo_check=True)
                .report_action(self)
            )
