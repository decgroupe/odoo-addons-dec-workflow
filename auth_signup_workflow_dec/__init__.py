from odoo import api, SUPERUSER_ID
from odoo.addons.tools_miscellaneous.tools import _, update_translation


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_translation(
        env,
        "auth_signup.mail_template_user_signup_account_created",
        {"subject": _("Account activated for ${object.company_id.portal_name}")},
    )
