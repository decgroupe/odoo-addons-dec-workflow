# -*- coding: utf-8 -*-
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

from datetime import datetime
from dateutil import relativedelta
from itertools import groupby
from operator import itemgetter

from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger(__name__)


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    @api.model
    def run(self, product_id, product_qty, product_uom, location_id, \
        name, origin, values):
        """ This method override existing one to catch UserError and call
        a custom implementation of _log_next_activity to redirect the error
        according to settings of this module.
        Redirection is built upon a regex string that is mapped to a user_id
        """
        res = False
        try:
            res = super().run(product_id, product_qty, product_uom, \
                location_id, name, origin, values)
        except UserError as error:
            _logger.info(error.name)
            raise

        return res

    # def _log_next_activity(self, product_id, note):
    #     existing_activity = self.env['mail.activity'].search([('res_id', '=',  product_id.product_tmpl_id.id), ('res_model_id', '=', self.env.ref('product.model_product_template').id),
    #                                                           ('note', '=', note)])
    #     if not existing_activity:
    #         # If the user deleted todo activity type.
    #         try:
    #             activity_type_id = self.env.ref('mail.mail_activity_data_todo').id
    #         except:
    #             activity_type_id = False
    #         self.env['mail.activity'].create({
    #             'activity_type_id': activity_type_id,
    #             'note': note,
    #             'user_id': product_id.responsible_id.id,
    #             'res_id': product_id.product_tmpl_id.id,
    #             'res_model_id': self.env.ref('product.model_product_template').id,
    #         })
