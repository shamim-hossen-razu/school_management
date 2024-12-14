from odoo import models, fields, api
from lxml import etree


class Teacher(models.Model):
    _name = 'school_management.teacher'
    _description = 'Teacher'
    _inherit = 'base.person'
    _parent_name = 'parent_id'
    _parent_store = True

    subject = fields.Selection([('Bangla', 'Bangla'), ('English', 'English'), ('Math', 'Math'), ('Science', 'Science'),
                                ('Social Science', 'Social Science'), ('Religion', 'Religion')])
    joining_date = fields.Date()
    parent_id = fields.Many2one('school_management.teacher', string='Reporting Manager', index=True, ondelete='cascade',
                                domain="[('subject', '=', subject)]")
    parent_path = fields.Char(index=True)
    path_name = fields.Char(compute='_compute_path_name', store=True)
    job_age = fields.Float(compute='_compute_job_age', store=True)
    subordinate_teacher_ids = fields.One2many('school_management.teacher', 'parent_id', string='Subordinate Teachers')

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
            return {'domain': {'parent_id': [('subject', '=', self.subject)]}}
        return {'domain': {'parent_id': []}}

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



