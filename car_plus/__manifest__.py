# -*- coding: utf-8 -*-
{
    'name': "CarPlus Client",

    'summary': """
        Mòdul per a la gestió dels lloguers/renting de vehicles.""",

    'description': """
        Aquest mòdul permet la gestió de clients, vehicles, factures i lloguer de vehicles.
    """,

    'author': "CarPlus",
    'website': "http://www.carplus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Cars',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/carPlus_client_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}