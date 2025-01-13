from odoo import models, fields, api
from lxml import etree


class Teacher(models.Model):
    _name = 'school_management.teacher'
    _description = 'Teacher'
    _inherit = 'base.person'
    _parent_name = 'parent_id'
    _parent_store = True

    school_id = fields.Many2one('school_management.school', string='School', ondelete='cascade')
    subject = fields.Selection([('Bangla', 'Bangla'), ('English', 'English'), ('Math', 'Math'), ('Science', 'Science'),
                                ('Social Science', 'Social Science'), ('Religion', 'Religion')], required=True)
    joining_date = fields.Date(default=fields.Date.today())
    parent_id = fields.Many2one('school_management.teacher', string='Reporting Manager', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    path_name = fields.Char(compute='_compute_path_name', store=True)
    job_age = fields.Float(string="Job Duration", compute='_compute_job_age', store=True, precompute=True)
    subordinate_teacher_ids = fields.One2many('school_management.teacher', 'parent_id', string='Subordinate Teachers')

    @api.onchange('parent_id')
    def _onchange_parent_id(self):
        if self.parent_id:
            self.subject = self.parent_id.subject
        return {
            'warning': {'title': "Warning", 'message': "What is this?", 'type': 'notification'},
        }

    def _compute_job_age(self):
        for record in self:
            if record.joining_date:
                record.job_age = (fields.Date.today() - record.joining_date).days / 365
            else:
                record.job_age = 0

    def _compute_path_name(self):
        for record in self:
            if record.parent_id:
                record.path_name = f"{record.parent_id.path_name} / {record.name}"
            else:
                record.path_name = record.name

    @api.onchange('subject')
    def _onchange_subject(self):
        if self.subject:
            # Define the domain based on the subject field
            return {
                'domain': {
                    'parent_id': [('subject', '=', self.subject)]
                    # Restrict parent_id to teachers with the same subject
                }
            }
        return {
            'domain': {
                'parent_id': []  # No restriction if no subject is selected
            }
        }

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name} ({record.subject})"

    def read(self, fields=None, load='_classic_read'):
        '''
            Override the read method to change the display_name to uppercase
            Usually triggered when the user reads the record
        '''
        res = super().read(fields=fields, load=load)
        if res and 'display_name' in res[0]:
            res[0]['display_name'] = res[0]['display_name'].upper()
        return res

    def create(self, vals):
        '''
            Override the create method to change the display_name to uppercase
            Usually triggered when the user creates a new record
        '''
        if 'display_name' in vals:
            vals['display_name'] = vals['display_name'].upper()
        return super().create(vals)

    def default_get(self, fields):
        '''
            Override the default_get method to change the display_name to uppercase
            Usually triggered when the user creates a new record
        '''
        res = super().default_get(fields)
        if 'display_name' in res:
            res['display_name'] = res['display_name'].upper()
        return res


