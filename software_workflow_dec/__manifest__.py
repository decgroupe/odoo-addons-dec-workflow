{
    "name": "Software workflow (DEC)",
    "version": "14.0.1.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "depends": [
        "software_license_pass",
        "auth_signup_delegate_fencing",  # for pass email template
        "portal_workflow_dec", # for portal_name
    ],
    "data": [
        "data/mail_template.xml",
        "data/ir_ui_view.xml",
    ],
    "installable": True,
    "force_post_init_hook": True,
    "post_init_hook": "post_init_hook",
}
