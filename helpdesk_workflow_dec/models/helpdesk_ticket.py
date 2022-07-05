# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Feb 2021

import re

from odoo import _, api, models, fields
from werkzeug import url_encode
from odoo.osv import expression


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'
    _order = 'number desc'

    @api.model
    def create(self, vals):
        if not vals.get('project_id'):
            project_support_id = self.env.ref(
                'helpdesk_workflow_dec.project_support'
            )
            vals['project_id'] = project_support_id.id
        ticket_id = super().create(vals)
        return ticket_id

    @api.multi
    @api.depends('name', 'number')
    def name_get(self):
        """ Custom naming to quickly identify a ticket
        """
        result = []
        for rec in self:
            name = ('[%s] %s') % (rec.number, rec.name)
            result.append((rec.id, name))
        return result

    @api.model
    def _name_search(
        self, name, args=None, operator='ilike', limit=100, name_get_uid=None
    ):
        if not args:
            args = []
        if name:
            positive_operators = ['=', 'ilike', '=ilike', 'like', '=like']
            record_ids = []
            if operator in positive_operators:
                record_ids = self._search(
                    [('number', '=', name)] + args,
                    limit=limit,
                    access_rights_uid=name_get_uid
                )
            if not record_ids and operator not in expression.NEGATIVE_TERM_OPERATORS:
                # Do not merge the 2 next lines into one single search, SQL
                # search performance would be abysmal on a database with
                # thousands of matching products, due to the huge merge+unique
                # needed for the OR operator (and given the fact that the
                # 'name' lookup results come from the ir.translation table
                # Performing a quick memory merge of ids in Python will give
                # much better performance
                record_ids = self._search(
                    args + [('number', operator, name)], limit=limit
                )
                if not limit or len(record_ids) < limit:
                    # we may underrun the limit because of dupes in the
                    # results, that's fine
                    limit2 = (limit - len(record_ids)) if limit else False
                    product2_ids = self._search(
                        args + [
                            ('name', operator, name),
                            ('id', 'not in', record_ids)
                        ],
                        limit=limit2,
                        access_rights_uid=name_get_uid
                    )
                    record_ids.extend(product2_ids)
            elif not record_ids and operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = expression.OR(
                    [
                        [
                            '&',
                            ('number', operator, name),
                            ('name', operator, name),
                        ],
                        [
                            '&',
                            ('number', '=', False),
                            ('name', operator, name),
                        ],
                    ]
                )
                domain = expression.AND([args, domain])
                record_ids = self._search(
                    domain, limit=limit, access_rights_uid=name_get_uid
                )
            if not record_ids and operator in positive_operators:
                ptrn = re.compile('(\[(.*?)\])')
                res = ptrn.search(name)
                if res:
                    record_ids = self._search(
                        [('number', '=', res.group(2))] + args,
                        limit=limit,
                        access_rights_uid=name_get_uid
                    )
        else:
            record_ids = self._search(
                args, limit=limit, access_rights_uid=name_get_uid
            )
        return self.browse(record_ids).name_get()

    def _compute_show_time_control(self):
        # Defined in module helpdesk_mgmt_timesheet_time_control
        result = super()._compute_show_time_control()
        for rec in self:
            rec.show_time_control = False
        return result
