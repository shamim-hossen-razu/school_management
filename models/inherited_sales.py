# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InheritedSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Binary(related='product_template_id.image_1920', string='Product Image',
                                  store=False, readonly=True)