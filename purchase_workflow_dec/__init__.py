from . import models

from odoo import api, SUPERUSER_ID
from odoo.addons.tools_miscellaneous.tools import _, update_translation


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_translation(
        env,
        "purchase.email_template_edi_purchase",
        {"subject": _("${object.company_id.name} RFQ (Ref ${object.name or 'n/a' })")},
    )
    update_translation(
        env,
        "purchase.email_template_edi_purchase_done",
        {
            "subject": _(
                "${object.company_id.name} Order (Ref ${object.name or 'n/a' })"
            )
        },
    )
