{
    'name': 'Product Form Quotation workflow (DEC)',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'https://www.decgroupe.com',
    'depends':
        [
            'product_form_sale_link',
            'product_form_purchase_link',
            # Note that these modules (`product_form_sale_link` and
            # `product_form_purchase_link`) already are a dependency for
            # `product_form_quotation_link`
            'product_form_quotation_link',
        ],
    'data': [
        'views/product_template.xml',
        'views/product_product.xml',
    ],
    'installable': True
}
