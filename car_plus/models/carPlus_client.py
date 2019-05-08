# -- coding: utf-8 --

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta, date


class Client(models.Model):
    _name = 'carplus.client'

    name = fields.Char(string="Nom")
    dni = fields.Char(string="DNI")
    dataNaixament = fields.Date(string="Data de naixement")
    targetaCredit = fields.Char(string="Targeta de crèdit")

    @api.onchange('dataNaixament')
    def onchange_date(self):
        if self.dataNaixament:
            today = date.today()
            born = datetime.strptime(self.dataNaixament, '%Y-%m-%d')
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            if age < 18:
                raise exceptions.UserError(
                    "Ho sentim, només podem oferir serveis a majors d'edat!"
                )
