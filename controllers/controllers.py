# -*- coding: utf-8 -*-
from odoo import http

class Books(http.Controller):
    # @http.route('/mylibrary/mylibrary', website=True, auth='public')
    # def index(self, **kw):
    #     return "Hello, world"

    #@http.route('/mylibrary/list', auth='user', website=True, method=['GET'], type='http')
    # @http.route('/mylibrary/listbook', auth='public')
    # def list(self, **kw):
    #     return http.request.render('mylibrary.list', {
    #         'books': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
    #     })

    @http.route('/mylibrary/listbook', auth='public', website=True)
    def list(self, **kw):
        books = http.request.env['mylib.book']
        return http.request.render('mylibrary.list', {
            'books': books.search([])
        })

    # @http.route('/mylibrary/<name>/', auth='public', website=True)
    # def book(self, name):
    #     return '<h1>{}</h1>'.format(name)

    # @http.route('/mylibrary/<int:id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    #
    @http.route('/mylibrary/<model("mylib.book"):book>/', auth='user', website=True)
    def list_model(self, book):
        # render(template-template để liên kết, qcontext=None-, lazy=True, **kw)
        return http.request.render('mylibrary.list1', {
            'Book': book
        })
    # @http.route('/mylibrary/list/', auth='user')
    # def list(self, **kw):
    #     return http.request.render('books.listing', {
    #         'root': '/books/books',
    #         'objects': http.request.env['books.books'].search([]),
    #     })
    # @http.route('/mylibrary/list/', auth='user')
    # def list(self, **kw):
    #     return http.request.render('books.listing', {
    #         'root': '/books/books',
    #         'objects': http.request.env['books.books'].search([]),
    #     })

#     @http.route('/books/books/objects/<model("books.books"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('books.object', {
#             'object': obj
#         })