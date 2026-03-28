# -*- coding: utf-8 -*-
{
    'name': "CRM",
    'author': "IDEA",
    'version': '16.0.0.0',
    'depends': ['base','crm','contacts_module','sale','sales_team'],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/crm_lead_views.xml",
        "views/product_product_views.xml",
        "views/res_users_views.xml",
        "views/menu.xml"
    ],
    'license': 'LGPL-3',
    'installable': True,

}
