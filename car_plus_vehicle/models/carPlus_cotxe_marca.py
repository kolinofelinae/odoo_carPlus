# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CotxeMarca(models.Model):
    _name = 'carplus.cotxemarca'

    name = fields.Char(string="Marca")