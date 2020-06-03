# -*- coding: utf-8 -*-

from odoo import fields, models

class Category(models.Model):
    _name = 'mylib.category'
    _description = 'My library categories'

    name = fields.Char("Tên danh mục")
    parent_category = fields.Many2one('mylib.category', 'Danh mục cha')
    description = fields.Text("Mô tả")
    books = fields.One2many(comodel_name='mylib.book',inverse_name='category_id',string="Danh sách sách")

    _sql_constraints = [
        ('unique_name', 'unique(name)', u'Tên danh mục đã tồn tại, hãy thử lại!'),] #ràng buộc tên danh mục không được trùng nhau.

