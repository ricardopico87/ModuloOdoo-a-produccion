# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CamposCalcPet(models.Model):
    _inherit = 'eje.pet'

    color_raro = fields.Boolean(string='Color Raro', compute='_compute_color_raro')
    piel = fields.Char(string='Piel', default='Green')


    @api.depends('piel')
    def _compute_color_raro(self):
        for record in self:
            record.color_raro = record.piel == 'Green'



