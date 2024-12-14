from odoo import models, fields


class Parent(models.Model):
    _name = 'school_management.parent'
    _description = 'Parent'
    _inherit = 'base.person'

    occupation = fields.Selection([('Service', 'Service'), ('Business', 'Business'), ('Housewife', 'Housewife'),
                                   ('Other', 'Other')], string='Date of Birth', default_export_compatible=True)
    annual_income = fields.Float()
