from . import models

from odoo import api, SUPERUSER_ID
from odoo.addons.tools_miscellaneous.tools import _, update_translation


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_translation(
        env,
        "calendar.calendar_template_meeting_invitation",
        {"subject": _("Invitation: ${object.event_id.name}")},
    )
    update_translation(
        env,
        "calendar.calendar_template_meeting_changedate",
        {
            "subject": _(
                "${'Invitation' if object.state != 'accepted' else 'Meeting'} updated: ${object.event_id.name}"
            )
        },
    )
    update_translation(
        env,
        "calendar.calendar_template_meeting_reminder",
        {
            "subject": _(
                "${'Invitation' if object.state != 'accepted' else 'Meeting'} reminder: ${object.event_id.name}"
            )
        },
    )
