# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2020

import logging

from odoo import _, models

_logger = logging.getLogger(__name__)


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _run_buy(self, procurements):
        alt_procurements = []
        # Ignore consumable when sourcing from production location
        for procurement, rule in procurements:
            prod_location = (
                procurement.location_id.get_warehouse()._get_production_location()
            )
            if (
                procurement.product_id.is_consumable
                and procurement.location_id == prod_location
            ):
                _logger.info(
                    _("Ignore consumable stock.rule for {}").format(
                        procurement.product_id.display_name,
                    )
                )
            else:
                alt_procurements.append((procurement, rule))
        return super()._run_buy(alt_procurements)
