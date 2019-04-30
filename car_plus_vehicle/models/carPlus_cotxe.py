# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cotxe(models.Model):
    _name = 'carplus.cotxe'

    marca = fields.Char(string="Marca")
    model = fields.Char(string="Model")
    color = fields.Char(string="Color")
    matricula = fields.Char(string="Matricula")
    data_compra = fields.Char(string="Data de compra")
    places = fields.Integer(string="Número de plaçes")
    tipus = fields.Char(string="Tipus")
    combustible = fields.Char(string="Combustible")
    preu_lloguer = fields.Float(string="Preu lloguer")
    preu_renting = fields.Float(string="Preu renting")
