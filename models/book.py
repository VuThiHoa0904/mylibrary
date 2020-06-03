# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class Book(models.Model):
    _name = 'mylib.book'
    _description = 'My library books'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name desc'

    name = fields.Char("Tên sách")
    name_seq = fields.Char(string='Book Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))

    def _get_default_code(self):
        return 0
    @api.multi
    def open_bookloan_book(self):
        return {
            'name': ('Danh sách người mượn'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [('book_id','=',self.id)],
            'res_model': 'mylib.bookloan_detail',
            'view_id': False,
            #'target': 'new',
            # 'views': False,
            'type': 'ir.actions.act_window',
            #'context': self.env.context,
        }

    code = fields.Char("Mã sách", default=_get_default_code)
    year = fields.Integer("Năm xuất bản")
    category_id = fields.Many2one(comodel_name='mylib.category', string="Danh mục sách")
    author = fields.Many2many(comodel_name='mylib.author', string="Tác giả")
    description = fields.Text("Mô tả sách")
    image = fields.Binary("Ảnh bìa")
    amount = fields.Integer("Số lượng", track_visibility='always') #track_visibility='always': lưu lại lịch sử khi thay đổi số lượng
    book = fields.Many2one(comodel_name='mylib.book',string="Sách của tôi", domain="[('year','<',2019),('year','>',2017)]")
    cost = fields.Float("Giá gốc", track_visibility='always') #track_visibility='always': lưu lại lịch sử khi thay đổi giá
    price = fields.Float(string="Giá bán",compute="_tinh_gia_ban")
    htm = fields.Html("Nội dung")
    bookloans = fields.One2many("mylib.bookloan_detail",inverse_name='book_id',string="Danh sách người mượn sách")
    state = fields.Selection(
        [('con', 'Còn sách'), ('saphet', 'Sắp hết'), ('het', 'Hết sách')], "Trạng thái")

    _sql_constraints = [
        ('unique_code', 'unique(code)', u'Mã sách đã tồn tại, hãy thử lại!'),
        ('unique_name', 'unique(name)', u'Tên sách đã tồn tại, hãy thử lại!'),
    ]
    bookloan_count = fields.Integer(string="Số lượng người mượn", compute='get_bookloan_count')

    @api.depends('bookloan_count')
    def get_bookloan_count(self):
        count = self.env['mylib.bookloan_detail'].search_count([('book_id','=',self.id)])
        for rec in self:
            rec.bookloan_count = count
    @api.constrains("code")
    def _code_validate(self):
        for book in self:
            if len(book.code) < 4:
                raise exceptions.ValidationError(u"Mã sách quá ngắn!")

    @api.constrains("amount") # bắt ngoại lệ khi nhập số lượng
    def _amount_validate(self):
        for book in self:
            if book.amount < 0:
                raise exceptions.ValidationError(u"Số lượng không thể ít hơn được nữa!")

    @api.onchange("amount") #sd để khi thêm nhập số lượng sách nhưng quên không chọn tình trạng thì tình trạng sách sẽ được tự cập nhập theo số lượng
    def _amount_onchange(self):
        for rec in self:
            if rec.amount == 0:
                rec.state = 'het'
            elif 0 < self.amount < 20:
                rec.state = 'saphet'
            else:
                rec.state = 'con'

    @api.depends("amount","cost")
    def _tinh_gia_ban(self):
        for book in self:
            if(book.amount>20):
                book.price = book.cost*1.5
            else:
                book.price = book.cost*2
    @api.model
    def _doi_trang_thai(self,sl):
        if sl==0:
            self.state = "het"
        elif 0<sl<20 :
            self.state = "saphet"
        else:
            self.state = "con"

    @api.onchange("amount")
    def _lay_trang_thai(self):
        for rec in self:
            rec._doi_trang_thai(self.amount)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', ('New')) == ('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('mylib.book.sequence') or ('New')
        result = super(Book, self).create(vals)
        return result
