# -*- coding: utf-8 -*-

from odoo import models, fields


class Avocat(models.Model):
    _name = "cabinet.avocat.avocat"
    _description = "Les Avocats"

    name = fields.Char(string="Nom et Prénom", required=True)
    situation_matrimoniale = fields.Selection(
        [
            ("celibataire", "Célibataire"),
            ("marie", "Mariée"),
            ("veuve", "Veuve"),
            ("divorce", "divorcée"),
        ],
        string="Situation Matrimoniale",
    )
    numero_bureau = fields.Char(string="Numéro de bureau")
    taux_horaire = fields.Float(string="Taux Horaire")
    speciality_id = fields.Many2one(
        "cabinet.avocat.speciality", string="Spécialité de l'avocat"
    )
    affaire_ids = fields.Many2many(
        "cabinet.avocat.affaire", string="liste des Affaires"
    )
