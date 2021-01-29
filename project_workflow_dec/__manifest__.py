{
    'name': 'Project Workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Custom views for project''',
    'depends': [
        'dec',
        'project_category',
        'web_kanban_draggable',
    ],
    'data': [
        'views/project_project.xml',
        'views/project_task.xml',
    ],
    'installable': True
}
