{
    'name': 'Purchase workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Purchase order",
    'depends':
        [
            'purchase',
            'purchase_order_line_stock_available',
            'web_widget_many2one_avatar',
        ],
    'data':
        [
            'views/assets.xml',
            'views/purchase_order.xml',
            'views/purchase_order_line.xml',
            'templates/mail.xml',
        ],
    'installable': True
}
