# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Report(models.Model):
    _name = 'carplus.report'

    client_id = fields.Many2one("carplus.client", string="Client")
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle")
    nom_segona_part = fields.Char(string="Nom segona part")
    dni_segona_part = fields.Char(string="DNI segona part")
    matricula_segona_part = fields.Char(string="Matrícula segona part")
    telefon_segona_part = fields.Char(string="Telefon segona part")
