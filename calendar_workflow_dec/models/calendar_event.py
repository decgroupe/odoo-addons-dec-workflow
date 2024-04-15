# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2022

from odoo import models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    # backport from Odoo 17.0
    def find_partner_customer(self):
        self.ensure_one()
        return next(
            (
                attendee.partner_id
                for attendee in self.attendee_ids.sorted("create_date")
                if attendee.partner_id != self.user_id.partner_id
            ),
            self.env["calendar.attendee"],
        )
