# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2022

from odoo import models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"
