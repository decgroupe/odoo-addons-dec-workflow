{
    'name': 'Helpdesk workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Helpdesk Support''',
    'depends': [
        'project_identification',
        'helpdesk_mgmt_timesheet',
    ],
    'data': [
        'data/project.xml',
        'views/helpdesk_ticket.xml',
    ],
    'installable': True
}
