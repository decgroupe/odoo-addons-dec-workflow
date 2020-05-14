{
    'name': 'Purchase workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Purchase order''',
    'depends': [
        'dec',
        'purchase'
    ],
    #'force_migration':'12.0.0.0.0',
    'data':
        [
            'views/purchase_order.xml',
        ],
    'installable': True
}
