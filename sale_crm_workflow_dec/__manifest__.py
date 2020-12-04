{
    'name': 'CRM Sale',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Show links between leads and sale orders''',
    'depends': [
        'sale_crm',
        'partner_academy',
    ],
    'data': [
        'views/crm_lead.xml',
        'views/sale_order.xml',
    ],
    'installable': True
}
