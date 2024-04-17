{
    "name": "Sale workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "category": "Sales",
    "depends": [
        "sale",
        "sale_margin",
        "sale_summary",
        "sale_warranty",
        "sale_delivery_rate",
        "web",
    ],
    "data": [
        "data/ir_ui_view.xml",
        "data/mail_template.xml",
        "views/sale_order.xml",
    ],
    "installable": True,
    "force_post_init_hook": True,
    "post_init_hook": "post_init_hook",
}
