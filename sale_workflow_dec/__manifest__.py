{
    'name': 'Sale workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'category': 'Sales',
    'summary': '''Custom views for sale order''',
    'depends': [
        'dec',
        'sale',
        'sale_summary',
        'sale_warranty',
    ],
    'data':
        [
            'data/mail_template.xml',
            'views/assets.xml',
            'views/sale_order.xml',
        ],
    'installable': True
}
