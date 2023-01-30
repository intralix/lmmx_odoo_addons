# -*- coding: utf-8 -*-
{
    'name': 'Logica Mobile México',
    'version': '15.0.1.0.0',
    'summary': 'Logica Mobile México internal processes',
    'sequence': 50,
    'website': 'https://www.logicamobilemexico.mx',
    'description': """
Logica Mobile Mexico
====================
This module provides to the company features for work with internal processes 

This module is maintained by internal developers.
    """,
    'author': 'LMMX',
    'installable': True,
    'application': True,
    'auto_install': False,
    'category': "Services/Lmmx",
    'depends': [
        'base',
        'mail',
        'stock',
        'contacts',
        'account',
        'sale_subscription',
        'helpdesk',
        'repair',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/cell_chip.xml',
        'views/custom_employee.xml',
    ],
    'license': "AGPL-3",
}
