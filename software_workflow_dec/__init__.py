from odoo import api, SUPERUSER_ID
from odoo.addons.tools_miscellaneous.tools import _, update_translation


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_translation(
        env,
        "software_license_pass.email_template_pass_send",
        {
            "subject": _(
                "e-space ${object.company_id.name} ${ctx['model_description']} (Ref ${object.name or 'n/a' })"
            )
        },
    )
