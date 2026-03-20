# -*- coding: utf-8 -*-

{
    "name": "Chambre des Notaires du Sénégal",
    "sequence": -200,
    "version": "18.0.1.0.0",
    "category": "TP",
    "summary": "Gestion complète des actes notariés et conformité juridique au Sénégal",
    "description": """Ce module Odoo est une solution métier dédiée aux notaires du Sénégal. 
        Il permet de digitaliser l'ensemble du cycle de vie d'un dossier notarial, 
        de l'ouverture du répertoire à l'archivage sécurisé.
        Fonctionnalités principales :
            - Gestion des Actes : Création et suivi des actes authentiques (Ventes immobilières, Successions, Constitutions de sociétés/SCI).
            - Calculateur de Frais : Automatisation du calcul des droits d'enregistrement, de la taxe de publicité foncière et des émoluments selon le barème officiel sénégalais.
            - Gestion du Répertoire : Tenue dématérialisée du répertoire électronique conformément aux exigences de la Chambre des Notaires.
            -  Suivi du Foncier : Intégration des étapes liées à la Conservation Foncière et au Cadastre.
            - Comptabilité Notariale : Gestion rigoureuse des comptes clients (fonds de tiers) et génération des états financiers spécifiques.""",
    "author": "Youssoupha LAM",
    "company": "MSI-UADB",
    "maintainer": "Equipe Master SI UADB",
    "website": "https://uadb.edu.sn/",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/acte.xml",
        "views/bien.xml",
        "views/client.xml",
        "views/dossier.xml",
        "views/menu.xml",
        "views/notaire.xml",
        "views/sequence.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
