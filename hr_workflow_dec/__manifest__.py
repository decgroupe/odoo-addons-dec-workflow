{
    'name': 'HR workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Human resources Support''',
    'depends': [
        'hr_timesheet',
        'hr_holidays',
    ],
    'data': [
        'views/hr_timesheet.xml',
        'views/hr_leave.xml',
        'views/hr_leave_allocation.xml',
    ],
    'installable': True
}
