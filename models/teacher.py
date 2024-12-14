from odoo import models, fields


class Teacher(models.Model):
    _name = 'school_management.teacher'
    _description = 'Teacher'
    _inherit = 'base.person'

    subject = fields.Selection([('Bangla', 'Bangla'), ('English', 'English'), ('Math', 'Math'), ('Science', 'Science'),
                                ('Social Science', 'Social Science'), ('Religion', 'Religion')])
    joining_date = fields.Date()
