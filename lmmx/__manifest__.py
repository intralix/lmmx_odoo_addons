# -*- coding: utf-8 -*-
{
    'name': 'Logica Mobile México',
    'description': 'Logica Mobile México module for internal processes',
    'author': 'LMMX',
    'application': True,
    'license': "AGPL-3",
    'website': 'https://www.logicamobilemexico.mx',
    'category': "Services/LmmX",
    'version': '15.0.1.0.0',
    'depends': [
        'base',
        'stock',
        'contacts',
        'account',        
        'crm',
        'sale_subscription',
        'helpdesk',
        'mail',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/cell_chip.xml',
    ],
}
