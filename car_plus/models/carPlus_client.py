# -- coding: utf-8 --

from odoo import models, fields, api, exceptions


class Client(models.Model):
    _name = 'carplus.client'

    name = fields.Char(string="Nom")
    dni = fields.Char(string="DNI")
    dataNaixament = fields.Date(string="Data de naixement")
    targetaCredit = fields.Char(string="Targeta de crèdit")

    @api.onchange('dataNaixament')
    def onchange_date(self):
        if self.dataNaixament and esMajorDedat(self):
            raise exceptions.UserError(
                "Ho sentim, només podem oferir serveis a majors d'edat!"
            )

    def esMajorDedat(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
