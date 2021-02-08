# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Feb 2021

from odoo import _, api, models, fields
from werkzeug import url_encode


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.model
    def create(self, vals):
        if not vals.get('project_id'):
            project_support_id = self.env.ref(
                'helpdesk_workflow_dec.project_support'
            )
            vals['project_id'] = project_support_id.id
        ticket_id = super().create(vals)
        return ticket_id
