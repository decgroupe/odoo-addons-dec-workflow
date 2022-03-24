# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2022

from odoo import _, api, models


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    @api.onchange('stop_datetime')
    def _onchange_stop_datetime(self):
        if self.start_datetime and self.stop_datetime:
            self.duration = self._get_duration(
                self.start_datetime, self.stop_datetime
            )
