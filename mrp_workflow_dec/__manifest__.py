{
    'name': 'Production workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Production order''',
    'depends': [
        'mrp',
        'stock_auto_validate',
        'purchase_stock',
    ],
    'data': [
        'data/stock_data.xml',
        'views/mrp_production.xml',
        'views/mrp_bom.xml',
    ],
    'installable': True
}
