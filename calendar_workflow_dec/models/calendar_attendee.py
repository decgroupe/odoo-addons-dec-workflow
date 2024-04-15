# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Apr 2024

from odoo import fields, models
from odoo.addons.base.models.res_partner import _tz_get


class CalendarAttendee(models.Model):
    _inherit = "calendar.attendee"

    # backport from Odoo 17.0
    mail_tz = fields.Selection(
        _tz_get,
        compute="_compute_mail_tz",
        help="Timezone used for displaying time in the mail template",
    )

    # backport from Odoo 17.0
    def _compute_mail_tz(self):
        for attendee in self:
            attendee.mail_tz = attendee.partner_id.tz
