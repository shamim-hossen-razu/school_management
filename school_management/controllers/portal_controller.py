from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request

class MySchoolPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(MySchoolPortal, self)._prepare_home_portal_values(counters)
        # values['school_count'] = request.env['school_management.school'].search_count([])
        values['school_count'] = 10
        print("values: ", values)
        return values
