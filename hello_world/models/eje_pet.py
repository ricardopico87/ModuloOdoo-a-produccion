# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EjePet(models.Model):
    _name = 'eje.pet'

    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age', required=True)
    code = fields.Char(string='code', default="New", readonly=1)
    color = fields.Char(string='color', required=True)
    is_new = fields.Boolean(string='is_new')
    type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('other', 'Other')], string='type', default="dog")

    @api.model
    def create(self, values):
        if values.get('code', "New") == "New":
            values['code'] = self.env['ir.sequence'].next_by_code(
                'eje.pet') or "Nuevo"
        pet = super(EjePet, self).create(values)
        return pet
