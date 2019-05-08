# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime, timedelta, date


class RentingLloguer(models.Model):
    _name = 'carplus.rentinglloguer'

    client_id = fields.Many2one("carplus.client", string="Client")
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle")
    is_renting = fields.Boolean(string="Marcar aquesta casella si es renting")
    data_inici = fields.Date(string="Data inici renting/lloguer")
    data_final = fields.Date(string="Data final renting/lloguer")

    @api.onchange('data_inici', 'data_final', 'is_renting')
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

        if self.is_renting and self.data_inici and self.data_final:
            initial_date = datetime.strptime(self.data_inici, '%Y-%m-%d')
            final_date = datetime.strptime(self.data_final, '%Y-%m-%d')
            if abs(final_date - initial_date).days > 30:
                raise exceptions.UserError(
                    "No es pot llogar un vehicle per més de 30 dies"
                )
        else:
            if self.is_renting == False and self.data_inici and self.data_final:
                initial_date = datetime.strptime(self.data_inici, '%Y-%m-%d')
                final_date = datetime.strptime(self.data_final, '%Y-%m-%d')
                if abs(final_date - initial_date).days < 30:
                    raise exceptions.UserError(
                        "No es pot fer renting d'un vehicle per menys de 30 dies"
                    )
                else:
                    if abs(final_date - initial_date).days > 730:
                        raise exceptions.UserError(
                            "No es pot fer renting d'un vehicle per mes de 2 anys"
                        )
