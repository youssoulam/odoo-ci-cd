# -*- coding: utf-8 -*-

from odoo import models, fields


class Audience(models.Model):
    _name = "cabinet.avocat.audience"
    _description = "Audiences des dossier"

    name = fields.Char(string="Référence du Dossier", required=True)
    date_audience = fields.Datetime(string="Date de l'audience")
    affaire_id = fields.Many2one("cabinet.avocat.affaire", string="Affaire liée")
