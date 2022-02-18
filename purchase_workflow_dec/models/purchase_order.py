# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    _order = "id desc"

    # Deprecated since web_widget_many2one_avatar
    partner_image_small = fields.Binary(
        related='partner_id.image_small',
        string='Supplier Logo',
    )

    @api.multi
    def action_rfq_send(self):
        view = super().action_rfq_send()
        # Do not set layout to "mail.mail_notification_paynow" since we
        # don't want that our supplier access our portal
        view['context']['custom_layout'] = \
            'purchase_workflow_dec.mail_notification_paynow_nobutton'
        return view
