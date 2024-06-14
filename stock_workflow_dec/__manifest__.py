{
    "name": "Stock workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "depends": [
        "stock",
        "stock_split_procure_method",
        "stock_mts_mto_rule",
    ],
    "data": [
        "data/stock_location.xml",
        "data/picking_type.xml",
        "data/stock_warehouse.xml",
        "views/assets.xml",
        "views/stock_move.xml",
        "views/stock_picking.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
    "force_post_init_hook": True,
}
