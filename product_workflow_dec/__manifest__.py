{
    'name': 'Product workflow (DEC)',
    'version': "14.0.1.0.0",
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'summary': "",
    'depends': [
        'product',
        'stock',
        'sale',
        'sale_stock',
    ],
    "external_dependencies": {
        "python": ["numpy", ]
    },
    'data': [
        'data/product_product.xml',
        'views/product_template.xml',
    ],
    'installable': True
}
