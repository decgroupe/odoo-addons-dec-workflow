{
    'name': 'Purchase workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Purchase order''',
    'depends': [
        'dec',
        'purchase',
        'purchase_order_line_stock_available',
    ],
    #'force_migration':'12.0.0.0.0',
    'data':
        [
            'views/assets.xml',
            'views/purchase_order.xml',
            'templates/mail.xml',
        ],
    'installable': True
}
