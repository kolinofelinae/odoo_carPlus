# -- coding: utf-8 --

from odoo import models, fields, api


class Client(models.Model):
    _name = 'carplus.client'

    nom = fields.Char(string="Nom")
    dni = fields.Char(string="DNI")
    dataNaixament = fields.Date(string="Data de naixement")
    targetaCredit = fields.Char(string="Targeta de crèdit")
