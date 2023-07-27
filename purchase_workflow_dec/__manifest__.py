{
    "name": "Purchase workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "summary": "Purchase order",
    "depends": [
        "purchase",
        "purchase_order_line_stock_available",
        "web",
    ],
    "data": [
        "views/assets.xml",
        "views/purchase_order.xml",
        "views/purchase_order_line.xml",
        "templates/mail.xml",
    ],
    "installable": True,
}
