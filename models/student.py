from odoo import models, fields, api
from odoo.exceptions import UserError


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

    # This method is invoked by the unlink method while deleting a record of this model
    # @api.ondelete(at_uninstall=False)
    # def _unlink_if_no_result(self):
    #
    #     x = self._read_group([('standard', '=', 9)], groupby=['section'], aggregates=['age:sum'],
    #                         having=[('age:sum', '>', 15)], offset=0, limit=None, order=None)
    #
    #     y = self.read_group([('standard', '=', 9)], fields=['age:sum'], groupby=['section'], offset=0, limit=None)
    #
    #     for record in self:
    #
    #         z = record.search_fetch([('age', '>', 15)], ['name', 'age'])
    #
    #         if record.school_id:
    #             raise UserError('Cannot delete a student with school.')

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



