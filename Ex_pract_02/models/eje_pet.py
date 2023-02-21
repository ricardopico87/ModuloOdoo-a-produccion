# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EjePet(models.Model):
    _inherit = 'eje.pet'

    is_pretty = fields.Boolean(string='Pretty Name')
    my_age = fields.Integer(string='My age')

    @api.onchange('my_age')
    def _onchange_account_type(self):
        if self.my_age:
            self.age = self.my_age

    @api.model
    def create(self, values):
        values['age'] = values["my_age"]
        # Add code here
        return super(EjePet, self).create(values)





