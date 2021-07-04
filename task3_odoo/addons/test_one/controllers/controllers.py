# -*- coding: utf-8 -*-
# from odoo import http


# class TestOne(http.Controller):
#     @http.route('/test_one/test_one/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_one/test_one/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_one.listing', {
#             'root': '/test_one/test_one',
#             'objects': http.request.env['test_one.test_one'].search([]),
#         })

#     @http.route('/test_one/test_one/objects/<model("test_one.test_one"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_one.object', {
#             'object': obj
#         })
