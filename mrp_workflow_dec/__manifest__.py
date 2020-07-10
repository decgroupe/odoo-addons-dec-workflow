{
    'name': 'Production workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Production order''',
    'depends': [
        'mrp',
        'stock_auto_validate',
    ],
    'data': ['views/mrp_production.xml', ],
    'installable': True
}
