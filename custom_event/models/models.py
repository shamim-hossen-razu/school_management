# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /opt/odoo/odoo_17_custom_addons/custom_event(models.Model):
#     _name = '/opt/odoo/odoo_17_custom_addons/custom_event./opt/odoo/odoo_17_custom_addons/custom_event'
#     _description = '/opt/odoo/odoo_17_custom_addons/custom_event./opt/odoo/odoo_17_custom_addons/custom_event'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

