{
    'name': 'Helpdesk workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Helpdesk Support''',
    'depends': [
        'project_identification',
        'helpdesk_mgmt_timesheet',
        'helpdesk_mgmt_timesheet_time_control',
    ],
    'data': [
        'data/project.xml',
        'views/helpdesk_ticket.xml',
    ],
    'installable': True
}
