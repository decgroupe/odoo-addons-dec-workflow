{
    'name': 'Stock workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': '''Stock and pickings''',
    'depends': [
        'dec',
        'stock',
        'stock_split_procure_method',
        'stock_mts_mto_rule',
    ],
    'data':
        [
            'data/picking_type.xml',
            'data/stock_location.xml',
            'data/stock_warehouse.xml',
            'views/assets.xml',
            'views/stock_move.xml',
            'views/stock_picking.xml',
        ],
    'installable': True
}
