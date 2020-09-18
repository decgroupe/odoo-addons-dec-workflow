# Use SQL query to by-pass check added by product module
def post_init(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})
    product_uom_hour = env.ref('uom.product_uom_hour')
    cr.execute(
        """
        UPDATE uom_uom
        SET factor=%s
        WHERE id=%s;
    """, (
            7.0,
            product_uom_hour.id,
        )
    )
