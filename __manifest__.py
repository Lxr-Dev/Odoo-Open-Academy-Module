# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Gestor de Cursos""",

    'description': """
        Un gestor de cursos a modo de práctica
    """,

    'author': "LxrDev",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/course.xml',
        'views/sessions.xml',
        'views/instructors.xml',
        'views/inscriptions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/open_academy_demo.xml',
    ],
}
