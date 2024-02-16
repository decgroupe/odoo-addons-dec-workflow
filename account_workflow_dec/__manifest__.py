{
    "name": "Account workflow (DEC)",
    "version": "14.0.2.0.0",
    "author": "DEC",
    "website": "https://www.decgroupe.com",
    "depends": [
        "account",
        "account_move_name_sequence", # OCA
    ],
    "data": [
        "views/account_invoice.xml",
        "views/account_invoice_line.xml",
    ],
    "installable": True,
}
