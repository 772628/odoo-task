{
    'name': "MRP Customization",
    'summary': """MRP Customization""",
    'description': """ MRP Customization """,
    'author': "Pranav Patel",
    'maintainer': 'Pranav Patel',
    'website': "",
    'version': '14.0.1.0.0',

    'depends': ['mrp'],

    # always loaded
    'data': [
        'views/bom.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}