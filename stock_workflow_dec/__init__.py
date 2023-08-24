from . import models

from odoo import api, SUPERUSER_ID


def _get_production_location(env, warehouse_id):
    company_id = warehouse_id.company_id
    domain = [("usage", "=", "production"), ("company_id", "=", company_id.id)]
    production_location = env["stock.location"].search(domain, limit=1)
    return production_location


def post_init_hook(cr, registry):
    """This hook is used to set the production location in newly added picking types.
    Previously, it was set from XML data using a reference to
    `stock.location_production`, but this has been removed since Odoo 14.0 because of
    multi-company behaviours.
    """
    env = api.Environment(cr, SUPERUSER_ID, {})

    picking_type_add = env.ref("stock_workflow_dec.picking_type_add")
    picking_type_add.default_location_dest_id = _get_production_location(
        env, picking_type_add.default_location_src_id.get_warehouse()
    )

    picking_type_return = env.ref("stock_workflow_dec.picking_type_return")
    picking_type_return.default_location_src_id = _get_production_location(
        env, picking_type_return.default_location_dest_id.get_warehouse()
    )
    picking_type_exceed = env.ref("stock_workflow_dec.picking_type_exceed")
    picking_type_exceed.default_location_src_id = _get_production_location(
        env, picking_type_exceed.default_location_dest_id.get_warehouse()
    )
