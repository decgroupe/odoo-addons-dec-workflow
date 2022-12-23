# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jul 2022

from odoo import _, api, models


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def message_notify(
        self,
        *,
        partner_ids=False,
        parent_id=False,
        model=False,
        res_id=False,
        author_id=None,
        email_from=None,
        body='',
        subject=False,
        **kwargs
    ):
        if body:
            if isinstance(body, bytes):
                body = body.decode('utf-8')
            body = self.env['mail.template']._hard_replace(body)
        super().message_notify(
            partner_ids=partner_ids,
            parent_id=parent_id,
            model=model,
            res_id=res_id,
            author_id=author_id,
            email_from=email_from,
            body=body,
            subject=subject,
            **kwargs
        )
