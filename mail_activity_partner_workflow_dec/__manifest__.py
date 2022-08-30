{
    'name': 'Mail Activity Partner Workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Customization",
    'depends':
        [
            "mail_activity_workflow_dec",
            "mail_activity_partner",
            "project_partner_location",
            "sale_partner_location",
        ],
    'data': ['views/mail_activity.xml', ],
    'installable': True
}
