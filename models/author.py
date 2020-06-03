# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Author(models.Model):
    _name = 'mylib.author'
    _description = 'My library authors'

    name = fields.Char("Tên")
    image = fields.Binary("Ảnh")
    nation = fields.Many2one('res.country', 'Quốc gia')
    description = fields.Text("Tiểu sử")

    @api.model #decorate cho model Author
    def create(self,vals): #vals: <class 'dict'>: {'name': 'xuân diệu', 'image': False, 'nation': 241, 'description': 'Nhà văn của thơ tình'}
        name = vals.get("name")
        new_name = name.title() # Đổi chữ đầu tiên trong tên sang chữ hoa
        vals["name"] = new_name
        self.env['mylib.contact'].create({'name': new_name})
        # Trả về phương tạo ban đàu của model bằng cách gọi supper, sau đó gọi đến phương thức create ban đầu của model Author và truyền vào gtri value mà mk mốn thay đổi
        return super(Author,self).create(vals) #gọi đệ quy create()
