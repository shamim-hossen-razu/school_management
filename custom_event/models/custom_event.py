from odoo import api, fields, models


class CustomEvent(models.Model):
    _name = 'custom.event'
    _description = 'Custom Event'

    name = fields.Char(string='Name')
    location = fields.Char(string='Location')
    date = fields.Date(string='Date')
