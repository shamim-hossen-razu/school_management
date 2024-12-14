from odoo import models, fields


class BasePerson(models.AbstractModel):
    _name = 'base.person'
    _description = 'Base Person'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    date_of_birth = fields.Date(string='Date of Birth', default_export_compatible=True)
