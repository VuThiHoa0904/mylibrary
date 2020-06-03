
from odoo import fields, models, api, exceptions

class BookLoan(models.Model):
    _name = "mylib.bookloan"
    _description = "Mượn sách"
    _rec_name = "user"

    code = fields.Char("Mã phiếu mượn")
    user = fields.Many2one('res.partner','Người mượn')
    date = fields.Datetime("Ngày mượn")
    date_return = fields.Datetime("Ngày trả")
    is_archived = fields.Boolean("Đã lưu trữ", groups="mylibrary.mylib_manager")
    bookloan_detail = fields.One2many(comodel_name="mylib.bookloan_detail", inverse_name="bookloan",string=u"Chi tiết phiếu mượn") #một phiếu mượn có thể có nhiều chi tiết phiếu mượn
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False,track_visibility='onchange', track_sequence=3,
        default='draft')
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
    def action_done(self):
        for rec in self:
            rec.state = 'done'
class BookLoanDetail(models.Model):
    _name = "mylib.bookloan_detail"
    _description = "Chi tiết phiếu mượn"
    _rec_name = 'bookloan'

    bookloan = fields.Many2one(comodel_name="mylib.bookloan",string="Người mượn") #một chi tiết phiếu mượn chỉ thuộc về 1 phiếu mượn
    book_id = fields.Many2one(comodel_name="mylib.book", string="Sách")
    amount = fields.Integer(string="Số lượng", default=1)


    # _sql_constraints = [
    #     ('unique_book_id', 'unique(book_id)', u'Sách đã tồn tại!'),
    # ]
    # @api.constrains("book_id")
    # def uniquie_book_id(self):
    #     for book in self:
    #         if unique(book.book_id):
    #             raise exceptions.ValidationError(u"Mã sách quá ngắn!")