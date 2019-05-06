# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class RentingLloguer(models.Model):
    _name = 'carplus.rentinglloguer'

    client_id = fields.Many2one("carplus.client", string="Client")
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle")
    is_renting = fields.Boolean(string="Marcar aquesta casella si es renting")
    data_inici = fields.Date(string="Data inici renting/lloguer")
    data_final = fields.Date(string="Data final renting/lloguer")

    @api.onchange('data_inici', 'data_final')
    def onchange_date(self):
        if self.data_inici and self.data_inici < fields.Date.today():
            self.data_inici = fields.Date.today()
            raise exceptions.UserError(
                "No es pot seleccionar una data abans d'avui"
            )

        if self.data_final and self.data_inici > self.data_final:
            raise exceptions.UserError(
                "No es pot seleccionar una data de finalització abans de la d'inici"
            )
