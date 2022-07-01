{
    'name': 'CRM (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "View customization",
    'depends': [
        'crm',
        'crm_timesheet',
        'web_kanban_draggable',
    ],
    'data': ['views/crm_lead.xml', ],
    'installable': True
}
