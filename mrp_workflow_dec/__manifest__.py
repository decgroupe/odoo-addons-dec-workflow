{
    'name': 'Production workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'depends': [
        'mrp',
        'stock_auto_validate',
        'purchase_stock',
        'product_small_supply',
    ],
    'data': [
        'data/stock_data.xml',
        'views/mrp_production.xml',
        'views/mrp_bom.xml',
        'views/mrp_workcenter.xml',
        'views/product_template.xml',
        'views/product_product.xml',
    ],
    'installable': True
}
