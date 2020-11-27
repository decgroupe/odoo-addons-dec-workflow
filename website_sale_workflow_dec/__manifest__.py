{
    'name': 'Website Sale workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': 'Website Sale',
    'depends': [
        'website_sale',
        'website_sale_main_category',
        'website_sale_tax_toggle',
        'website_megamenu',
    ],
    'data': [
        'views/assets.xml',
        'views/product.xml',
        'views/product_carousel.xml',
        'views/tax_toggle.xml',
        'views/product_price.xml',
    ],
    'installable': True
}
