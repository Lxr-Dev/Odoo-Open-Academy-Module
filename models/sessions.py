# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sessions(models.Model):
    _name = 'open_academy.session'
    _description = 'Sesiones'

    # name = fields.Char(string='Nombre del Instructor', required=True)
    name = fields.Many2one('open_academy.instructor', string='Instructor', required=True, ondelete='cascade')
    course = fields.Many2one('open_academy.course', string="Curso", required=True, ondelete='cascade')
    startDate = fields.Date(string='Fecha de Inicio')
    duration = fields.Integer(string="Duración (Horas)", default=1)
    numberOfSeats = fields.Integer(string="Número de Asientos", default=20)

    @api.depends('numberOfSeats')
    def availableSeats(self):
        for record in self:
            totalEntries = self.env['open_academy.inscription'].search_count([('course', '=',record.course.id )])
            record.seatsAvailable = 100.00 - (totalEntries*(100/record.numberOfSeats))

    @api.depends('numberOfSeats')
    def _get_attendees_count(self):
        for record in self:
            record.attendees = self.env['open_academy.inscription'].search_count([('course', '=',record.course.id )])

    seatsAvailable = fields.Float(compute=availableSeats, string="Porcentaje de Asientos Disponibles", store=False , recompute=True, default=100.0)
    attendees = fields.Integer(string="Total de Inscripciones", compute='_get_attendees_count', store=True, default=0)
    