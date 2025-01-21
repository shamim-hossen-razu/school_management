from odoo import api, fields, models, _


class StudentDataUpdate(models.TransientModel):
    _name = 'student.data.update.wizard'
    _description = 'Student Data Update'

    weight_in_kg = fields.Float()
    weight_in_pounds = fields.Float()

    def update_data(self):
        active_ids = self.env.context.get('active_ids', [])
        active_model = self.env.context.get('active_model')

        if active_model and active_ids:
            records = self.env[active_model].browse(active_ids)
            for record in records:
                record.write({
                    'weight_in_kg': self.weight_in_kg,
                    'weight_in_pounds': self.weight_in_pounds,
                })

