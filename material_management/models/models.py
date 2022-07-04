# -*- coding: utf-8 -*-

from odoo import api, fields, models

class materialSupplier(models.Model):
    
    _name = "material.supplier"
    _description = 'Material Supplier'
    _order = "name"

    name = fields.Char('Name', required=True)
    
class materialInformation(models.Model):
    
    _name = "material.information"
    _description = 'Material Information'
    _order = "name"

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton','Cotton')], 'Type', default='fabric', required=True)
    buying_price = fields.Float(string='Buy Price', default=100.0, digits=(3, 2), required=True)
    supplier_id  = fields.Many2one('material.supplier', 'Related Supplier', required=True)
    
    @api.multi
    def _check_buying_price(self):
        for record in self:
            if record.buying_price < 100:
                return False
        return True
    
    _constraints = [
        (_check_buying_price, 'Buying price can\'t be less than 100!', ['buying_price'])
    ]