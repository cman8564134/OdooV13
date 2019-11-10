# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.openacademy'
    _description = 'Open Academy class'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text("Description")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
