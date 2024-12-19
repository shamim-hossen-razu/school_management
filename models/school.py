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

    def create(self, vals):
        # create record of related model school_management.teacher by the  command triple (CREATE, 0, values)
        new_teacher_list = [
            (0, 0, {'name': 'Teacher 1', 'subject': 'Bangla', 'school_id': self.id}),
            (0, 0, {'name': 'Teacher 2', 'subject': 'English', 'school_id': self.id}),
            (0, 0, {'name': 'Teacher 3', 'subject': 'Math', 'school_id': self.id}),
        ]
        if not vals.get('teacher_ids'):
            vals['teacher_ids'] = new_teacher_list

        # create record of related model school_management.student by the  command triple (CREATE, 0, values)
        new_student_list = [
            (0, 0, {'name': 'Student 1', 'roll_number': '001', 'school_id': self.id}),
            (0, 0, {'name': 'Student 2', 'roll_number': '002', 'school_id': self.id}),
            (0, 0, {'name': 'Student 3', 'roll_number': '003', 'school_id': self.id}),
        ]
        if not vals.get('student_ids'):
            vals['student_ids'] = new_student_list
        return super(School, self).create(vals)


