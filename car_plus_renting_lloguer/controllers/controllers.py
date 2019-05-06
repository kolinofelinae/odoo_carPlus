# -*- coding: utf-8 -*-
from odoo import http

# class CarPlus(http.Controller):
#     @http.route('/car_plus/car_plus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_plus/car_plus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_plus.listing', {
#             'root': '/car_plus/car_plus',
#             'objects': http.request.env['car_plus.car_plus'].search([]),
#         })

#     @http.route('/car_plus/car_plus/objects/<model("car_plus.car_plus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_plus.object', {
#             'object': obj
#         })