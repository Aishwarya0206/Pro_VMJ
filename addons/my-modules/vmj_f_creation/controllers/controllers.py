# -*- coding: utf-8 -*-
# from odoo import http


# class VmjFCreation(http.Controller):
#     @http.route('/vmj_f_creation/vmj_f_creation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vmj_f_creation/vmj_f_creation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vmj_f_creation.listing', {
#             'root': '/vmj_f_creation/vmj_f_creation',
#             'objects': http.request.env['vmj_f_creation.vmj_f_creation'].search([]),
#         })

#     @http.route('/vmj_f_creation/vmj_f_creation/objects/<model("vmj_f_creation.vmj_f_creation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vmj_f_creation.object', {
#             'object': obj
#         })
