{
    'name': 'UoM Workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "Custom hour/day ratio",
    'depends': ['uom', ],
    "data": ['data/uom.xml', ],
    'installable': True,
    'post_init_hook': 'post_init',
}
