{
    'name': 'Project Workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Custom views for project",
    'depends':
        [
            'dec',
            'hr_timesheet',
            'sale_timesheet',
            'sale_timesheet_line_exclude',
            'sale_timesheet_task_exclude',
            'project_category',
            'project_identification',
            'web_kanban_draggable',
            'web_widget_many2one_avatar',
        ],
    'data':
        [
            'views/assets.xml',
            'views/project_project.xml',
            'views/project_task.xml',
            'data/project_type.xml',
            'data/project.xml',
            'data/project_task_type.xml',
            'data/project_task.xml',
            'data/project_tags.xml',
        ],
    'installable': True
}
