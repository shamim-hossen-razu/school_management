from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'school_management.course'
    _description = 'Course'

    name = fields.Char()
    code = fields.Char(copy=False, string='Course Code', required=True)
    standard = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                 ('8', '8'), ('9', '9'), ('10', '10')], copy=False)
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

    def create(self, vals):
        if 'standard' in vals:
            students = self.env['school_management.student'].search([('standard', '=', vals['standard'])])
            student_commands = [(4, student.id, 0) for student in students]  # The '4' command links existing records

            vals['student_ids'] = student_commands
        return super(Course, self).create(vals)

    def write(self, vals):
        if 'standard' in vals:
            # Unlink the existing students (remove the current links)
            vals['student_ids'] = [(5, 0, 0)]  # This unlinks all existing students

            # Search for students based on the new 'standard'
            students = self.env['school_management.student'].search([('standard', '=', vals['standard'])])

            # Create a list of commands to link the new students
            student_commands = [(4, student.id, 0) for student in students]

            # Add the new student links to the vals
            vals['student_ids'] += student_commands
            print(vals['student_ids'])

        # Call the super method to perform the write operation
        return super(Course, self).write(vals)

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super(Course, self).name_search(name=name, args=args, operator=operator, limit=limit)
        context = self.env.context
        print('Context', context)
        result_ids = context.get('result_ids', [])
        result_model = self.env['school_management.result']
        course_ids = []
        if result_ids:
            results = result_model.browse(result_ids)
            print('Results', results)
            for result in results:
                if result.course_id:
                    course_ids.append((result.course_id.id, result.course_id.name))
        print('Results', result_ids)
        print('Courses', course_ids)
        return res

