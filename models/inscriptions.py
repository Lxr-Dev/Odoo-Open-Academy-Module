# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions 

class Inscriptions(models.Model):
    _name = 'open_academy.inscription'
    _description = 'Inscripciones'

    name = fields.Char(string='Alumno', required=True)
    course = fields.Many2one('open_academy.course', string="Curso", required=True, ondelete='cascade')
    session = fields.Many2one('open_academy.session', string="Sesión", required=True, ondelete='cascade')

    @api.onchange('course')
    def onchangeCourse(self):
        for record in self:
            return {'domain': {'session': [('course','=',record.course.id)]}}

    @api.constrains('session')
    def _check_seats(self):
        for record in self:
            seats = record.session.numberOfSeats
            totalEntries = self.env['open_academy.inscription'].search_count([('course', '=',record.course.id )])
            if(seats < totalEntries):
                raise exceptions.ValidationError("Se han Agotado los asientos para esta Sesión")
            else:
                record.session.attendees += 1