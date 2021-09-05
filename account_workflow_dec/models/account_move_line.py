# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, May 2020

from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.multi
    @api.depends('ref', 'move_id')
    def name_get(self):
        """ Override name_get to print company_invoice_number for quicker line
            identification
        """
        result = []
        for line in self:
            value = line.move_id.name or ''
            if line.ref:
                value += '({})'.format(line.ref)
                if line.invoice_id.company_invoice_number:
                    value += '[{}]'.format(line.invoice_id.company_invoice_number)
            result.append((line.id, value))
        return result
