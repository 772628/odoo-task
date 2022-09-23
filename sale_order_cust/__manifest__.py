{
    'name': "Sale Customization",
    'summary': """Sale Customization""",
    'description': """ Sale Customization """,
    'author': "Pranav Patel",
    'maintainer': 'Pranav Patel',
    'website': "",
    'version': '14.0.1.0.0',

    'depends': ['sale_management','website_sale'],

    # always loaded
    'data': [
        'views/partner.xml',
        'views/template.xml',
        'views/sale.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}