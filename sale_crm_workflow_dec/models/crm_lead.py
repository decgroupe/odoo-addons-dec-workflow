# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <y.papouin at dec-industrie.com>, Dec 2020

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    partner_academy_id = fields.Many2one(
        related='partner_id.academy_id',
        string='Academy',
        store=True,
        oldname='partner_academy'
    )
