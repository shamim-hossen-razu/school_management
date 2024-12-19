from odoo import models, fields, api


class School(models.Model):
    _name = 'school_management.school'
    _description = 'School'

    name = fields.Char()
    address = fields.Text()
    contact = fields.Char()
    email = fields.Char()
    website = fields.Char()
    established_date = fields.Date()
    school_code = fields.Char()
    teacher_ids = fields.One2many('school_management.teacher', 'school_id', string='Teachers')
    student_ids = fields.One2many('school_management.student', 'school_id', string='Students')
    active = fields.Boolean(default=True)