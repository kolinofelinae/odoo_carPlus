# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Factura(models.Model):
    _name = 'carplus.factura'

    client_id = fields.Many2one("carplus.client", string="Client", required=True)
    vehicle_id = fields.Many2one("carplus.cotxe", string="Vehicle", required=True)
    renting_id = fields.Many2one("carplus.rentinglloguer", string="Contracte", required=True)
    data_factura = fields.Date(string="Data de factura", required=True)
    preu = fields.Float(string="Preu")

    # @api.onchange('renting_id')
    # def onchange_date(self):
    #     priceAply = 0.0
    #     if self.renting_id:
    #         for vehicle in self.browse(cr, uid, ids, context=context):
    #             if vehicle.preu_lloguer:
    #                 val = vehicle.preu_lloguer
    #                 raise exceptions.UserError(
    #                     "Valor --> " + val
    #                 )
