{
    'name': 'Sale workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'category': 'Sales',
    'summary': "Custom views for sale order",
    'depends': [
        'dec',
        'sale',
        'sale_summary',
        'sale_warranty',
        'web_widget_many2one_avatar',
    ],
    'data':
        [
            'data/mail_template.xml',
            'views/sale_order.xml',
        ],
    'installable': True
}
