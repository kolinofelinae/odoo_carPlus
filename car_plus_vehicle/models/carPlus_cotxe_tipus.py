# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CotxeTipus(models.Model):
    _name = 'carplus.cotxetipus'

    name = fields.Char(string="Tipus")
