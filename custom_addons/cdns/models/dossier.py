# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DossierClient(models.Model):
    _name = "cdns.dossier"
    _description = "Liste des Dossiers"

    name = fields.Char(string="N° Dossier", required=True)
    date_ouverture = fields.Date(string="Date d'ouverture")

    objet = fields.Selection(
        [
            ("vente", "Vente"),
            ("succession", "Succession"),
            ("heritage", "Héritage"),
            ("bail", "Bail"),
        ],
        string="Objet",
    )

    frais_dossier = fields.Float(string="Frais de dossier", required=True)

    notaire_id = fields.Many2one("cdns.notaire", string="Notaire Assigné")

    client_id = fields.Many2one("cdns.client", string="Client lié")

    status = fields.Selection(
        [
            ("nouveau", "Nouveau"),
            ("encours", "En cours"),
            ("traite", "Traité"),
            ("archive", "Archivé"),
        ],
        default="nouveau",
        string="Statut",
    )

    # ---------------------------------------
    # SMART BUTTON
    # ---------------------------------------

    document_count = fields.Integer(
        string="Nombre de documents", compute="_compute_document_count"
    )

    @api.depends()
    def _compute_document_count(self):
        for rec in self:
            rec.document_count = self.env["ir.attachment"].search_count(
                [("res_model", "=", "cdns.dossier"), ("res_id", "=", rec.id)]
            )

    # ---------------------------------------
    # BOUTONS WORKFLOW
    # ---------------------------------------

    def action_start(self):
        for rec in self:
            rec.status = "encours"

    def action_done(self):
        for rec in self:
            rec.status = "traite"

    def action_archive(self):
        for rec in self:
            rec.status = "archive"

    # ---------------------------------------
    # ACTION SMART BUTTON
    # ---------------------------------------

    def action_view_documents(self):

        return {
            "type": "ir.actions.act_window",
            "name": "Documents",
            "res_model": "ir.attachment",
            "view_mode": "list,form",
            "domain": [
                ("res_model", "=", "cdns.dossier"),
                ("res_id", "=", self.id),
            ],
        }
