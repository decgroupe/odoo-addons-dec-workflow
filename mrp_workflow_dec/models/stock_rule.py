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
# Written by Yann Papouin <y.papouin@dec-industrie.com>, Jul 2020

import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class StockRule(models.Model):
    _inherit = 'stock.rule'

    @api.multi
    def _run_buy(self, product_id, product_qty, product_uom, location_id, \
        name, origin, values):
        # Ignore consumable when sourcing from production location
        prod_location = location_id.get_warehouse()._get_production_location()
        if product_id.type == 'consu' and location_id == prod_location:
            _logger.info(
                "Ignore consumable stock.rule for {}".format(
                    product_id.display_name,
                )
            )
        else:
            super()._run_buy(
                product_id,
                product_qty,
                product_uom,
                location_id,
                name,
                origin,
                values,
            )
