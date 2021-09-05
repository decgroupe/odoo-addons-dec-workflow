{
    'name': 'CRM Sale',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Show links between leads and sale orders''',
    'depends': [
        'sale_crm',
    ],
    'data': [
        'views/crm_lead.xml',
        'views/sale_order.xml',
    ],
    'installable': True
}
