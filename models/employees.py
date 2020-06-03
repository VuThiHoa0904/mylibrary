from odoo import models,fields,api, exceptions

class Contact(models.Model):
    _name = 'mylib.contact'
    _description = "Thông tin liên lạc"
    _rec_name = 'name'
    name = fields.Char(string="Tên" )
    phone = fields.Char(string="Số điện thoại")
    address = fields.Char(string="Địa chỉ" )
    employee = fields.One2many(comodel_name="mylib.staff", inverse_name="contact",string=u"Nhân viên")

    @api.constrains("phone")
    def _phone_lenght(self):
        for employee in self:
            if len(employee.phone)<10:
                raise exceptions.ValidationError("Số điện thoại không hợp lệ")

class Employee(models.Model):
    _name = 'mylib.staff'
    _description = 'My library employees'
    _inherit = 'mylib.author'
    _inherits = {'mylib.contact': 'contact'}

    contact = fields.Many2one(comodel_name="mylib.contact", ondelete="cascade",string="Liên lạc")  # ondelete="cascade": Khi xóa 1 liên hệ thì nhân viên cũng bị xóa luôn
    name = fields.Char(related='contact.name', inherited=True) #Đảm bảo khi 1 tên thay đổi thì tên của contact cũng thay đổi theo, related nối quan hệ đến trường name trong contact
    phone = fields.Char(related="contact.phone", inherited=True)
    address = fields.Char(related="contact.address", inherited=True)
    gender = fields.Selection(string="Giới tính", selection=[('1', 'Nam'), ('2', 'Nữ'), ], required=False, )
    description = fields.Text("Ghi chú")



