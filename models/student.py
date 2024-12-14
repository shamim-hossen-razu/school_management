from odoo import models, fields


class Student(models.Model):
    _name = 'school_management.student'
    _description = 'Student'
    _inherit = 'base.person'
    _sql_constraints = [
        ('unique_roll_number', 'unique(roll_number,standard)', 'Roll number must be unique.')
    ]
    _order = 'roll_number desc'

    roll_number = fields.Char(copy=False)
    standard = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                 ('8', '8'), ('9', '9'), ('10', '10')], copy=False)
    section = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    version = fields.Selection([('Bangla', 'Bangla'), ('English', 'English')])
    admission_date = fields.Date(string='Admission Date')
    group = fields.Selection([('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts')])
