from odoo.addons.portal.controllers.portal import CustomerPortal


class MySchoolPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(MySchoolPortal, self)._prepare_home_portal_values(counters)
        print("values: ", values)
        return values
