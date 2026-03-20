# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date


class ClientNotaire(models.Model):
    _name = "cdns.client"
    _description = "Liste des Clients"
    _inherit = ["image.mixin"]

    name = fields.Char(string="Nom ou Dénomination sociale", required=True)
    type_client = fields.Selection(
        [("personne", "Personne"), ("entreprise", "Entreprise")],
        string="Type de Client",
        required=True,
        default="entreprise",
    )

    # Personne physique
    date_naissance = fields.Date(string="Date de Naissance")
    lieu_naissance = fields.Char(string="Lieu de Naissance")
    telephone_mobile = fields.Char(string="Numéro Portable")
    nationalite = fields.Many2one("res.country", string="Nationalité")
    numero_identite = fields.Char(string="N° CNI ou Passeport")
    situation_matrimoniale = fields.Selection(
        [
            ("celibataire", "Célibataire"),
            ("marie", "Marié(e)"),
            ("divorce", "Divorcé(e)"),
            ("veuf_veuve", "Veuf/Veuve"),
        ],
        string="Situation matrimoniale",
    )

    # Entreprise
    rccm = fields.Char(string="N° RCCM")
    ninea = fields.Char(string="N° NINEA")
    forme_juridique = fields.Selection(
        [("gie", "GIE"), ("sarl", "SARL"), ("sa", "SA"), ("sci", "SCI")],
        string="Forme Juridique",
    )

    # Adresse structurée (commune aux deux types)
    street = fields.Char(string="Rue")
    street2 = fields.Char(string="Complément d'adresse")
    zip = fields.Char(string="Code Postal")
    city = fields.Char(string="Ville")
    state_id = fields.Many2one("res.country.state", string="Province/État")
    country_id = fields.Many2one("res.country", string="Pays")

    # Pièces jointes
    piece_ids = fields.One2many(
        comodel_name="ir.attachment",
        inverse_name="res_id",
        string="Pièces jointes",
        domain=[("res_model", "=", "cdns.client")],
    )
    piece_count = fields.Integer(
        string="Documents", compute="_compute_piece_count")

    @api.depends("piece_ids")
    def _compute_piece_count(self):
        for rec in self:
            rec.piece_count = len(rec.piece_ids)

    def action_view_documents(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Documents",
            "res_model": "ir.attachment",
            "view_mode": "list,form",
            "domain": [("id", "in", self.piece_ids.ids)],
        }

    @api.constrains("date_naissance")
    def _check_date_naissance(self):
        for record in self:
            if record.date_naissance and record.date_naissance > date.today():
                raise ValidationError(
                    _(
                        "La date de naissance ne peut pas être supérieure à la date du jour."
                    )
                )
