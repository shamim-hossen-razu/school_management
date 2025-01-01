from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class BasePerson(models.AbstractModel):
    _name = 'base.person'
    _description = 'Base Person'

    name = fields.Char()
    age = fields.Float(compute='_compute_age', store=True, precompute=False, inverse='_inverse_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    date_of_birth = fields.Date(string='Date of Birth', default_export_compatible=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = (fields.Date.today() - record.date_of_birth).days / 365
            else:
                record.age = 0

    def _inverse_age(self):
        for record in self:
            if record.age:
                # Use relativedelta to accurately calculate the date_of_birth from age
                today = fields.Date.today()
                birth_date = today - relativedelta(years=record.age)
                record.date_of_birth = birth_date
            else:
                # If age is 0, set the date_of_birth to today (or any default date)
                record.date_of_birth = fields.Date.today()



