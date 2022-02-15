{
    'name': 'HR workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Human resources Support",
    'depends': [
        'hr_timesheet',
        'hr_holidays',
        'hr_timesheet_exclude',
        'hr_timesheet_task_stage',
        'hr_expense_easy',
        'sale_expense',
    ],
    'data': [
        'views/hr_expense_sheet.xml',
        'views/hr_timesheet.xml',
        'views/hr_leave.xml',
        'views/hr_leave_allocation.xml',
        'views/hr_employee.xml',
        'views/account_analytic_line.xml',
    ],
    'installable': True
}
