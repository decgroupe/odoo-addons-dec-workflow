# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Oct 2020

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # Override default report with aeroo one

    def do_print_picking(self):
        super().do_print_picking()
        return self.env.ref("stock_report_aeroo.stock_picking_report").report_action(
            self
        )
