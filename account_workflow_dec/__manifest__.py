{
    'name': 'Account workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'depends': [
        'account',
        'account_cancel',
    ],
    #'force_migration':'12.0.0.0.0',
    'data':
        [
            'views/assets.xml',
            'views/account_invoice.xml',
        ],
    'installable': True
}
