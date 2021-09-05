{
    'name': 'Production workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Production order''',
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
    ],
    'installable': True
}
