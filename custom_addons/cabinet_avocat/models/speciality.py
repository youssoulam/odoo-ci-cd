# -*- coding: utf-8 -*-

from odoo import models, fields


class Specialite(models.Model):
    _name = "cabinet.avocat.speciality"
    _description = "Spécialité"

    name = fields.Char(string="Spécialité", required=True)
    nombre_avocat = fields.Integer(string="Nobre d'avocat")
    avocat_ids = fields.One2many(
        "cabinet.avocat.avocat", "speciality_id", string="Liste des avocats"
    )
