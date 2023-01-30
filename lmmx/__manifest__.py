# -*- coding: utf-8 -*-
{
    'name': 'Logica Mobile México',
    'version': '15.0.1.0.0',
    'summary': 'Logica Mobile México module for internal processes',
    'website': 'https://www.logicamobilemexico.mx',
    'description': 'Logica Mobile México module for internal processes',
    'author': 'LMMX',
    'application': True,
    'license': "AGPL-3",
    'category': "Services/Lmmx",
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/cell_chip.xml',
    ],
}
