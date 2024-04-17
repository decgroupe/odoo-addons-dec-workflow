{
    "name": "Calendar workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "depends": [
        "calendar",
        "mail_qweb",
    ],
    "data": [
        "data/ir_ui_view.xml",
        "data/mail_template.xml",
        "views/assets.xml",
        "views/calendar.xml",
    ],
    "installable": True,
    "force_post_init_hook": True,
    "post_init_hook": "post_init_hook",
}
