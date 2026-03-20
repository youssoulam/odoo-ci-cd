# -*- coding: utf-8 -*-

from odoo import models, fields


class Affaire(models.Model):
    _name = "cabinet.avocat.affaire"
    _description = "Affaires des Clients"

    name = fields.Char(string="Référence du Dossier", required=True)
    titre = fields.Char(string="Titre de l'affaire", required=True)
    client_id = fields.Many2one("cabinet.avocat.client", string="Client de l'affaire")
    avocat_ids = fields.Many2many("cabinet.avocat.avocat", string="Liste des avocats")
    type_procedure = fields.Selection(
        [
            ("contentieux", "Contentieux"),
            ("conseil", "Conseil"),
            ("arbitrage", "Arbitrage"),
        ],
        string="Type de procédure",
    )
    status = fields.Selection(
        [
            ("brouillon", "Brouillon"),
            ("encours", "En cours"),
            ("plaidoirie", "Plaidoirie"),
            ("clôture", "Clôturé"),
        ],
        string="Type de procédure",
    )
