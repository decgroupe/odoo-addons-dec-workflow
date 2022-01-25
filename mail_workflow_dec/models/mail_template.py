# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Jan 2022

from lxml import html as htmltree
import re
from odoo import _, api, models


class MailTemplate(models.Model):
    _inherit = "mail.template"

    @api.model
    def _hard_replace(self, html):
        #TODO: Create model/view with customizable before/after lines
        to_replace = [
            (r'#875A7B', r'#414141'),
            (r'border-radius: 3px', r'border-radius: 0px'),
            (r'border-radius: 5px', r'border-radius: 0px'),
        ]
        for before, after in to_replace:
            html = re.sub(before, after, html)
        return html

    @api.model
    def render_post_process(self, html):
        html = super().render_post_process(html)
        return self._hard_replace(html)

    @api.multi
    def send_mail(
        self,
        res_id,
        force_send=False,
        raise_exception=False,
        email_values=None,
        notif_layout=False
    ):
        """ When `notif_layout` is `False`, no `render_post_process` is
            called. That's why we need to override `generate_email`
        """
        return super(
            MailTemplate,
            self.with_context(hard_replace_generate_email=not notif_layout)
        ).send_mail(
            res_id, force_send, raise_exception, email_values, notif_layout
        )

    @api.multi
    def generate_email(self, res_ids, fields=None):
        res = super().generate_email(res_ids, fields)
        if self.env.context.get('hard_replace_generate_email'
                               ) and res.get('body_html'):
            res['body_html'] = self._hard_replace(res.get('body_html'))
        return res
