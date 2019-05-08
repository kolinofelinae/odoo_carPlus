# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime


class Cotxe(models.Model):
    _name = 'carplus.cotxe'

    marca_id = fields.Many2one("carplus.cotxemarca", string="Marca", required=True)
    model = fields.Char(string="Model", required=True)
    color = fields.Char(string="Color")
    name = fields.Char(string="Matricula", required=True)
    data_compra = fields.Date(string="Data de compra", required=True)
    places = fields.Integer(string="Número de plaçes", required=True)
    tipus_id = fields.Many2one("carplus.cotxetipus", string="Tipus", required=True)
    combustible_id = fields.Many2one("carplus.cotxecombustible", string="Combustible", required=True)
    preu_lloguer = fields.Float(string="Preu lloguer", required=True)
    preu_renting = fields.Float(string="Preu renting", required=True)

    @api.onchange('data_compra')
    def onchange_date(self):
        if self.data_compra:
            date = datetime.strptime(self.data_compra, '%Y-%m-%d')
            today = datetime.strptime(fields.Date.today(), '%Y-%m-%d')
            if date > today:
                self.data_compra = today
                raise exceptions.UserError(
                    "No es pot seleccionar una data de compra mes gran que la d'avui"
                )
