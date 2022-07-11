# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2022

from odoo import _, api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def message_notify(self, partner_ids, body='', subject=False, **kwargs):
        if body:
            body = self.env['mail.template']._hard_replace(body)
        super().message_notify(
            partner_ids, body=body, subject=subject, **kwargs
        )
