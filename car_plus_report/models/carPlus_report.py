# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Report(models.Model):
    _name = 'carplus.report'

    client_id = fields.Many2one("carplus.client", string="Client", required=True)
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle", required=True)
    nom_segona_part = fields.Char(string="Nom segona part", required=True)
    dni_segona_part = fields.Char(string="DNI segona part", required=True)
    matricula_segona_part = fields.Char(string="Matrícula segona part", required=True)
    telefon_segona_part = fields.Char(string="Telefon segona part", required=True)
