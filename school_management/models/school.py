from odoo import models, fields, api


class Playground(models.Model):
    _name = 'school_management.playground'
    _description = 'Playground'

    name = fields.Char()
    location = fields.Char()
    area = fields.Float()
    type = fields.Selection([('indoor', 'Indoor'), ('outdoor', 'Outdoor')], default='outdoor')


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
    image = fields.Binary()
    color = fields.Char()
    established_date = fields.Date()
    school_code = fields.Char()
    teacher_ids = fields.One2many('school_management.teacher', 'school_id', string='Teachers', ondelete='cascade')
    student_ids = fields.One2many('school_management.student', 'school_id', string='Students', ondelete='cascade')
    active = fields.Boolean(default=True)
    playground_ids = fields.Many2many('school_management.playground', string='Playgrounds')
    swimming_pool_ids = fields.Many2many('school_management.swimming_pool', 'school_id', string='Swimming Pools')

    def print_school_report(self):
        return self.env.ref('school_management.school_management_school_report_action').report_action(self)

    def print_school_student_count_report(self):
        data = {'count': len(self.student_ids)}
        return self.env.ref('school_management.school_management_school_student_count_report_action').report_action(
            self, data=data)

    def return_action_to_open_student_list(self):
        action = self.env.ref('school_management.school_management_student_action').read()[0]
        action['domain'] = [('school_id', '=', self.id)]
        action['context'] = {'default_school_id': self.id}
        action['views'] = [(self.env.ref('school_management.school_management_student_view_tree').id, 'tree')]
        return action
