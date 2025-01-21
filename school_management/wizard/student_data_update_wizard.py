from odoo import api, fields, models, _


class StudentDataUpdate(models.TransientModel):
    _name = 'student.data.update.wizard'
    _description = 'Student Data Update'

    weight_in_kg = fields.Float()
    weight_in_pounds = fields.Float()

    def update_data(self):
        pass

