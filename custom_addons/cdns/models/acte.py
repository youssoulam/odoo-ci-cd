# -*- coding: utf-8 -*-

from odoo import models, fields, api, _ 
from datetime import date


class ActeNoatarie(models.Model):
    _name = "cdns.acte"
    _description = "Liste des Actes Notariés"

    name = fields.Char(
        string="N° de l'acte",
        readonly=True,
        copy=False,
        default=lambda self: _("Nouveau"),
    )
    date_acte = fields.Date(string="Date de signature", default=date.today())
    type_acte = fields.Selection(
        [
            ("vente", "Vente"),
            ("succession", "Succession"),
            ("donation", "Donation"),
            ("hypotheque", "Hypothèque"),
        ],
        string="Type Acte Notarié",
    )
    montant = fields.Float(string="Montant de l'Acte", required=True)
    dossier_id = fields.Many2one("cdns.dossier", string="Dossier lié")
    bien_ids = fields.Many2many("cdns.bien", string="Biens associés")
    status = fields.Selection(
        [
            ("nouveau", "Nouveau"),
            ("encours", "En cours"),
            ("traite", "Traité"),
            ("archive", "Archivé"),
        ],
        string="Statut",
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", _("Nouveau")) == _("Nouveau"):
                vals["name"] = self.env["ir.sequence"].next_by_code("cdns.acte") or _(
                    "Nouveau"
                )
        return super().create(vals_list)
