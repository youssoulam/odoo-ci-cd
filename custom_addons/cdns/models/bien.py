# -*- coding: utf-8 -*-

from odoo import models, fields


class BienImmobilier(models.Model):
    _name = "cdns.bien"
    _description = "Liste des Biens Immobiliers"

    name = fields.Char(string="Référence du Cadastre", required=True)
    type_bien = fields.Selection(
        [("terrain", "Terrain"), ("maison", "Maison"), ("immeuble", "Immeuble")],
        string="Type de Bien",
    )
    valeur_estime = fields.Float(string="Valeur Estimée", required=True)
    superficie = fields.Float(string="Superficie", required=True)
    acte_ids = fields.Many2many("cdns.acte", string="Actes liés")
