# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Client(models.Model):
    _inherit = 'carplus.client'

    factura_id = fields.Many2one("carplus.factura")
