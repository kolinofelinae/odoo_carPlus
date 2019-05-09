# -- coding: utf-8 --

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta, date


class Client(models.Model):
    _name = 'carplus.client'

    name = fields.Char(string="Nom", required=True)
    dni = fields.Char(string="DNI", required=True)
    dataNaixament = fields.Date(string="Data de naixement", required=True)
    targetaCredit = fields.Char(string="Targeta de crèdit", required=True)

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
