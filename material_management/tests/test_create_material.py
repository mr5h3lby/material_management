# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class materialInformation(TransactionCase):
    def setUp(self):
        super(materialInformation, self).setUp()
        self.supplier_a = self.env['material.supplier'].create({
            'name': 'Supplier A'
        })

    def test_create_material_success(self):
        # Create fabric material
        self.env['material.information'].create({
            'name': 'Fabric A',
            'code': 'FaA',
            'type': 'fabric',
            'buying_price': 150,
            'supplier_id': self.supplier_a.id
        })

    def test_create_material_unsuccess(self):
        # Create fabric material
        with self.assertRaises(ValidationError):
            self.env['material.information'].create({
                'name': 'Jeans A',
                'code': 'JeA',
                'type': 'jeans',
                'buying_price': 99.9,
                'supplier_id': self.supplier_a.id
            })