{
    'name': 'Stock workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Stock and pickings''',
    'depends': [
        'dec',
        'stock',
        'stock_split_procure_method',
    ],
    #'force_migration':'12.0.0.0.0',
    'data':
        [
            'data/picking_type.xml',
            'views/assets.xml',
            'views/stock_move.xml',
            'views/stock_picking.xml',
        ],
    'installable': True
}
