from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'school_management.course'
    _description = 'Course'

    name = fields.Char()
    code = fields.Char(copy=False, string='Course Code', required=True)
    teacher_ids = fields.Many2many('school_management.teacher', relation="teachers_courses_rel",
                                   column1='course_id', column2='teacher_id', string='Course Teachers')
    student_ids = fields.Many2many('school_management.student', string='Students')

    # Check unique code
    @api.constrains('code')
    def _check_code(self):
        for record in self:
            if self.search_count([('code', '=', record.code)]) > 1:
                raise ValidationError('Code must be unique.')

    @api.onchange('name', 'code')
    def _onchange_name(self):
        if self.name:
            self.name = self.name.upper()
        if self.code:
            self.code = self.code.upper()
