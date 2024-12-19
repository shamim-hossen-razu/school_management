from odoo import models, fields, api


class Student(models.Model):
    _name = 'school_management.student'
    _description = 'Student'
    _inherit = 'base.person'
    _sql_constraints = [
        ('unique_roll_number', 'unique(roll_number,standard)', 'Roll number must be unique.')
    ]
    _order = 'roll_number desc'

    school_id = fields.Many2one('school_management.school', string='School')
    roll_number = fields.Char(copy=False)
    standard = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                 ('8', '8'), ('9', '9'), ('10', '10')], copy=False)
    section = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    version = fields.Selection([('Bangla', 'Bangla'), ('English', 'English')])
    admission_date = fields.Date(string='Admission Date')
    group = fields.Selection([('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts')])
    weight_in_kg = fields.Float()
    weight_in_pounds = fields.Float()
    parent_id = fields.Many2one('school_management.parent', string='Parent')
    active = fields.Boolean(default=True)
    parent_name = fields.Char(related='parent_id.name', string='Parent Name', store=True)

    @api.onchange('weight_in_kg')
    def _onchange_weight_in_kg(self):
        if self.weight_in_kg:
            self.weight_in_pounds = self.weight_in_kg * 2.20462


