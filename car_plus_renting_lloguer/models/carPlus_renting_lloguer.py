# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentingLloguer(models.Model):
    _name = 'carplus.rentinglloguer'

    client_id = fields.Many2one("carplus.client", string="Client")
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle")
    is_renting = fields.Boolean(string="Marcar aquesta casella si es renting")
    data_inici = fields.Date(string="Data inici renting/lloguer")
    data_final = fields.Date(string="Data final renting/lloguer")
