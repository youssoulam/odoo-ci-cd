# -*- coding: utf-8 -*-

{
    "name": "Cabinet d'Avocat",
    "sequence": 0,
    "version": "18.0.1.0.0",
    "category": "TP",
    "summary": "Premier réalisé dans le cours ERP Odoo",
    "description": """Ce module permet de gérer un cabinet d'avocat 
    Les fonctionnalités du modules sont:
    - Gestion des avocats 
    - Gestion des clients 
    - Gestion des affaires
    - Gestion des audiences""",
    "author": "Youssoupha LAM",
    "company": "UADB",
    "maintainer": "Equipe IT UADB",
    "website": "https://uadb.edu.sn/",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/affaire.xml",
        "views/audience.xml",
        "views/avocat.xml",
        "views/client.xml",
        "views/speciality.xml",
        "views/menu.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
