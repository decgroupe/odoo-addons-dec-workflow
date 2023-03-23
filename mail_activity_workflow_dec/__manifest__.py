{
    'name': 'Mail activity workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''View customization''',
    'depends': [
        'mail',
        'mail_activity_board',
        'mail_activity_team',
    ],
    'data': [
        'views/mail_activity.xml',
        'data/mail_activity_team.xml',
    ],
    'installable': True
}
