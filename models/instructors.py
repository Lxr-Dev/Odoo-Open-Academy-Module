# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Instructors(models.Model):
    _name = 'open_academy.instructor'
    _description = 'Instructores'

    name = fields.Char(string='Nombre', required=True)
    identity = fields.Char(string='Identificación', required=True)

    _sql_constraints = [
        ('identity_unique','unique(identity)','El número de Identificación ya Existe')
    ]
    