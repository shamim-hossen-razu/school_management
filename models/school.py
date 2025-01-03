from odoo import models, fields, api


class Playground(models.Model):
    _name = 'school_management.playground'
    _description = 'Playground'

    name = fields.Char()
    location = fields.Char()


class SwimmingPool(models.Model):
    _name = 'school_management.swimming_pool'
    _description = 'Swimming Pool'

    name = fields.Char()
    location = fields.Char()
    length = fields.Float()
    width = fields.Float()
    depth = fields.Float()


class School(models.Model):
    _name = 'school_management.school'
    _description = 'School'

    name = fields.Char()
    address = fields.Text()
    contact = fields.Char()
    email = fields.Char()
    website = fields.Char()
    color = fields.Char()
    established_date = fields.Date()
    school_code = fields.Char()
    teacher_ids = fields.One2many('school_management.teacher', 'school_id', string='Teachers', ondelete='cascade')
    student_ids = fields.One2many('school_management.student', 'school_id', string='Students', ondelete='cascade')
    active = fields.Boolean(default=True)
    playground_ids = fields.Many2many('school_management.playground', string='Playgrounds')
    swimming_pool_ids = fields.Many2many('school_management.swimming_pool', 'school_id', string='Swimming Pools')




