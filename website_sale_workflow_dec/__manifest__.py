{
    "name": "Website Sale workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "depends": [
        "website_sale",
        "website_sale_main_category",
        "website_sale_tax_toggle",
        "website",
        "website_sale_hide_price",
        # "website_sale_product_public_code", # disable for migration
    ],
    "data": [
        "views/assets.xml",
        "views/product.xml",
        "views/product_carousel.xml",
        "views/tax_toggle.xml",
        "views/product_price.xml",
    ],
    "installable": True,
}
