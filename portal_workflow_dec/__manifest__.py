{
    "name": "Portal workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "summary": "Portal",
    "depends": [
        "portal",
        "mail_workflow_dec",
    ],
    "data": [
        "data/ir_ui_view.xml",
        "data/portal.xml",
    ],
    "installable": True,
    "force_post_init_hook": True,
    "post_init_hook": "post_init_hook",
}
