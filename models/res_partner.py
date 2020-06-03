from odoo import models,fields,api

class Partner(models.Model):
    _inherit = 'res.partner'

    isBlackList = fields.Boolean("Thuộc danh sách đen ")
    website = fields.Char(default="imus.com")

    @api.model
    def create(self, vals_list):
        res = super(Partner,self).create(vals_list)
        print("ok bb")
        return res