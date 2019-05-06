# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cotxe(models.Model):
    _inherit = 'carplus.cotxe'

    factura_id = fields.Many2one("carplus.factura")
