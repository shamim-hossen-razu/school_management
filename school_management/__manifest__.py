# -*- coding: utf-8 -*-
{
    'name': "School Management System",

    'summary': "This module help school to manage their students, teachers and parents and their information.",

    'description': """
        Long description of module's purpose
    """,

    'author': "Shamim Hossen",
    'website': "https://www.myschool.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/school_management.student.csv',
        'data/student_data.xml',
        'data/school_management.parent.csv',
        'views/student.xml',
        'views/student_result.xml',
        'views/course.xml',
        'views/playground.xml',
        'views/school.xml',
        'views/menus.xml',
        'views/sale_order_line_inherited.xml',
        'report/sale_report_template_inherited.xml',
        'report/school_report.xml',
        'report/basic_report_template.xml',
        'views/email_templates.xml',
        'report/sale_order_proposal_templates.xml',
        'report/sale_order_proposal_report_action.xml',
        # 'report/inherited_templates.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/student_data.xml',
    # ],
    'web.assets_backend': [
        'school_management/static/src/js/custom_kanban_renderer.js',
        'school_management/static/src/js/custom_kanban_view.js',
    ],
}
