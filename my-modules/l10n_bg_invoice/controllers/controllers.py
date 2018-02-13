# -*- coding: utf-8 -*-
from odoo import http

# class L10nBgInvoice(http.Controller):
#     @http.route('/l10n_bg_invoice/l10n_bg_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_bg_invoice/l10n_bg_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_bg_invoice.listing', {
#             'root': '/l10n_bg_invoice/l10n_bg_invoice',
#             'objects': http.request.env['l10n_bg_invoice.l10n_bg_invoice'].search([]),
#         })

#     @http.route('/l10n_bg_invoice/l10n_bg_invoice/objects/<model("l10n_bg_invoice.l10n_bg_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_bg_invoice.object', {
#             'object': obj
#         })