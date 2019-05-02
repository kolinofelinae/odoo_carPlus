# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Factura(models.Model):
    _name = 'carplus.factura'

    client_id = fields.Many2one("carplus.client", string="Client")
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle")
    preu = fields.Float(string="Preu")
    data_factura = fields.Date(string="Data de factura")
