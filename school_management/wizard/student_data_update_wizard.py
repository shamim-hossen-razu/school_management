from odoo import api, fields, models, _


class StudentDataUpdate(models.TransientModel):
    _name = 'student.data.update.wizard'
    _description = 'Student Data Update'

    weight_in_kg = fields.Float()
    weight_in_pounds = fields.Float()

    def update_data(self):
        print('Context_data', self.env.context.get('active_ids'))
        print('Context_data', self._context['active_ids'])
        print('Active id', self.env.context.get('active_id'))
        print('Active id', self._context['active_id'])
        print('Active model', self.env.context.get('active_model'))
        pass

