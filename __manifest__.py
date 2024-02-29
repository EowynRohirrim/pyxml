# -*- coding: utf-8 -*-
{
    'name': "alquilercoches",

    'summary': """
        Modulo dedicado al alquiler de coches""",

    'description': """
        Es un módulo dedica a la gestión de alquiler de vehículos en el que se va a usar clientes, coches, categorias y reservas
    """,

    'author': "PB",
    'website': "http://www.alquilauncoche.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Alquiler',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
