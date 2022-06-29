{
    'name': 'Web workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': 'Web',
    'depends': [
        'auth_signup',
        'auth_unique_link',
    ],
    'data': [
        'views/assets.xml',
        'templates/login_templates.xml',
    ],
    'installable': True
}
