from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    number_of_seat_per_standard = fields.Integer(string='Number of Seat Per Standard', config_parameter='school_management.number_of_seat_per_standard')
    number_of_seats_per_section = fields.Integer(string='Number of Seats Per Section', config_parameter='school_management.number_of_seats_per_section')

