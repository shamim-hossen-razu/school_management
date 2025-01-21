from odoo import models, fields, api
from odoo.exceptions import UserError


class Student(models.Model):
    _name = 'school_management.student'
    _description = 'Student'
    _inherit = ['base.person', 'mail.thread', 'mail.activity.mixin']
    _sql_constraints = [
        ('unique_roll_number', 'unique(roll_number,standard)', 'Roll number must be unique.')
    ]
    _order = 'roll_number desc'

    school_id = fields.Many2one('school_management.school', string='School')
    roll_number = fields.Char(copy=False)
    standard = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),
                                 ('8', '8'), ('9', '9'), ('10', '10')], copy=False)
    section = fields.Selection([('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'),])
    version = fields.Selection([('Bangla', 'Bangla'), ('English', 'English')])
    admission_date = fields.Date(string='Admission Date')
    group = fields.Selection([('Science', 'Science'), ('Commerce', 'Commerce'), ('Arts', 'Arts')])
    weight_in_kg = fields.Float()
    weight_in_pounds = fields.Float()
    parent_id = fields.Many2one('school_management.parent', string='Parent')
    active = fields.Boolean(default=True)
    parent_name = fields.Char(related='parent_id.name', string='Parent Name', store=True)
    result_ids = fields.One2many('school_management.result', 'student_id', string='Results')
    student_image = fields.Binary(string='Student Image')

    @api.onchange('weight_in_kg')
    def _onchange_weight_in_kg(self):
        if self.weight_in_kg:
            self.weight_in_pounds = self.weight_in_kg * 2.20462

    def write(self, vals):
        if self.student_image:
            file_size = self.with_context(bin_size=True).student_image
            if file_size:
                file_size = file_size.decode('utf-8')
                file_size = file_size.split(' ')
                if (file_size[1] == 'Kb' and float(file_size[0]) > 1024) or (
                        file_size[1] == 'Mb' and float(file_size[0]) > 10):
                    raise UserError('Image size cannot exceed 10 MB')
        return super(Student, self).write(vals)

    def custom_log(self):
        self.message_post(body='Custom log message')
        print(self.env.context)
        print(self._context)

    @api.model
    def _assign_group(self, *args, **kwargs):
        section_mapping = {
            'A': ('Science', 'English'),
            'B': ('Commerce', 'English'),
            'C': ('Arts', 'English'),
            'D': ('Science', 'Bangla'),
            'E': ('Commerce', 'Bangla'),
            'F': ('Arts', 'Bangla')
        }

        for student in self:
            if student.standard in ['9', '10']:
                if student.section in section_mapping:
                    student.group, student.version = section_mapping[student.section]

    def action_on_click(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student',
            'res_model': 'school_management.student',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }

    def send_email(self):
        self.env.ref('school_management.student_email_template').send_mail(self.id)

    def action_update_data(self):
        # i have to return this action by searching with ref :student_data_def action_update_data(self):
        action = self.env.ref('school_management.student_data_update_wizard_action').read()[0]
        print(type(action))
        print(action)
        return self.env.ref('school_management.student_data_update_wizard_action').read()[0]


