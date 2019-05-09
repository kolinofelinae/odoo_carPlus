# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RentingLloguer(models.Model):
    _inherit = 'carplus.rentinglloguer'

    factura_id = fields.Many2one("carplus.factura")
