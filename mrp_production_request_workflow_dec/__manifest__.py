{
    'name': 'MRP Production Request Workflow',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Group customization''',
    'depends': ['mrp_production_request', ],
    'data':
        [
            "security/model_security.xml",
            "security/ir.model.access.csv",
        ],
    'installable': True
}
