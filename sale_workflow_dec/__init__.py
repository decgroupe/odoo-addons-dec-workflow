from . import models

from odoo import api, SUPERUSER_ID
from odoo.addons.tools_miscellaneous.tools import _, update_translation


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    update_translation(
        env,
        "sale.email_template_edi_sale",
        {
            "subject": _(
                "${object.company_id.name} ${object.state in ('draft', 'sent') and (ctx.get('proforma') and 'Proforma' or 'Quotation') or 'Order'} ${object.name} (Ref ${object.client_order_ref or 'n/a' })"
            )
        },
    )
