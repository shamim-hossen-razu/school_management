from odoo import models, fields, api


class Result(models.Model):
    _name = 'school_management.result'
    _description = 'Result'
    _inherits = {'school_management.student': 'student_id'}

    student_id = fields.Many2one('school_management.student', string='Student', required=True, ondelete='cascade')
    course_id = fields.Many2one('school_management.course', string='Course', required=True)
    grade = fields.Selection([('a+', 'A+'), ('a', 'A'), ('a-', 'A-'), ('b+', 'B+'), ('b', 'B'), ('b-', 'B-'),])
    marks = fields.Float()
    result_date = fields.Date(string='Result Date')