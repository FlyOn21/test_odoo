# -*- coding: utf-8 -*-
from odoo import models, fields


class test_one(models.Model):
    _name = 'test_one.test_one'
    _description = 'test_one.test_one'

    name = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Integer()
    tester = fields.Many2one(comodel_name="res.partner", ondelete="set null")

