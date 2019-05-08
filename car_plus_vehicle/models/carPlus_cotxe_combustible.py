# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CotxeCombustible(models.Model):
    _name = 'carplus.cotxecombustible'

    name = fields.Char(string="Combustible")
