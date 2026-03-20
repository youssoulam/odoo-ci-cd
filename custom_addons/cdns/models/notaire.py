# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Notaires(models.Model):
    _name = "cdns.notaire"
    _description = "Liste des Notaires"

    name = fields.Char(string="Nom complet", compute="_compute_name", store=True)
    prenom = fields.Char(string="Prénom", required=True)
    nom_famille = fields.Char(string="Nom de famille", required=True)
    numero_agrement = fields.Char(string="Numéro d'agrément", required=True)
    date_nomination = fields.Date(string="Date de nomination")
    numero_telephone = fields.Char(
        string="Numéro de téléphone", placeholder="+221 77 654 87 40"
    )
    adresse_email = fields.Char(string="Email", placeholder="exemple@gmail.com")
    sexe = fields.Selection(
        [("male", "Masculin"), ("femelle", "Féminin")], string="Sexe"
    )
    dossier_ids = fields.One2many(
        "cdns.dossier", "notaire_id", string="Liste des dossiers"
    )
    nombre_dossier = fields.Integer(
        string="Nombre de dossier", compute="_compute_nombre_dossier", store=True
    )

    @api.depends("dossier_ids")
    def _compute_nombre_dossier(self):
        for rec in self:
            rec.nombre_dossier = len(rec.dossier_ids)

    @api.depends("prenom", "nom_famille")
    def _compute_name(self):
        for record in self:
            record.name = (record.prenom or "") + " " + (record.nom_famille or "")

    @api.onchange("nom_famille")
    def _onchange_nom_famille(self):
        if self.nom_famille:
            self.nom_famille = self.nom_famille.upper()

    @api.constrains("prenom", "nom_famille")
    def _check_preno_nom(self):
        for record in self:
            if record.prenom and record.nom_famille:
                if record.prenom.upper() == record.nom_famille.upper():
                    raise ValidationError(
                        "Le prénom doit être différent du nom de famille"
                    )
