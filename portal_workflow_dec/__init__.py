from . import models

from odoo import api, SUPERUSER_ID
from odoo.addons.tools_miscellaneous.tools import _, update_translation


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_translation(
        env,
        "portal.mail_template_data_portal_welcome",
        {"subject": _("Your access to ${object.user_id.company_id.portal_name}")},
    )
