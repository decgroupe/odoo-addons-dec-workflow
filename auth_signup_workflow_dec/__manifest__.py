{
    "name": "Signup workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "category": "Discuss",
    "depends": [
        "mail_workflow_dec",
        "portal_workflow_dec",
    ],
    "data": [
        "data/ir_ui_view.xml",
        "data/mail_template.xml",
    ],
    "installable": True,
    "force_post_init_hook": True,
    "post_init_hook": "post_init_hook",
}
