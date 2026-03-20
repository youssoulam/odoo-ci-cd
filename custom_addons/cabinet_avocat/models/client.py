# -*- coding: utf-8 -*-

from odoo import models, fields


class Client(models.Model):
    _name = "cabinet.avocat.client"
    _description = "Les Clients"

    name = fields.Char(string="Nom et ou Raison Sociale", required=True)
    type_client = fields.Selection(
        [
            ("personne", "Particulier"),
            ("entreprise", "Société"),
        ],
        string="Type de Client",
    )
    email = fields.Char(string="Email")
    phone = fields.Char(string="Téléphone")
    adress = fields.Char(string="Adresse")
    affaire_ids = fields.One2many(
        "cabinet.avocat.affaire", "client_id", string="Liste des affaires"
    )
