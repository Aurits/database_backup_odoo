# -*- coding: utf-8 -*-
# from odoo import http


# class DatabaseBackup(http.Controller):
#     @http.route('/database_backup/database_backup', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/database_backup/database_backup/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('database_backup.listing', {
#             'root': '/database_backup/database_backup',
#             'objects': http.request.env['database_backup.database_backup'].search([]),
#         })

#     @http.route('/database_backup/database_backup/objects/<model("database_backup.database_backup"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('database_backup.object', {
#             'object': obj
#         })

