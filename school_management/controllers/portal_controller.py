from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http

class MySchoolPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(MySchoolPortal, self)._prepare_home_portal_values(counters)
        values['school_count'] = request.env['school_management.school'].search_count([])
        print("values: ", values)
        return values

    @http.route(['/my/school', '/my/school/page/<int:page>'], type='http', auth='user', website=True)
    def my_school_list(self, page=1, **kw):
        school_count = request.env['school_management.school'].search_count([])
        pager = request.website.pager(url='/my/school', total=school_count, page=page, step=5, scope=5, url_args={})
        schools = request.env['school_management.school'].search([], limit=5, offset=pager['offset'])
        return request.render('school_management.school_list_view_template', {
            'schools': schools,
            'page_name': 'my_school',
            'pager': pager
        })

    @http.route(['/my/school/<int:school_id>'], type='http', auth='user', website=True)
    def my_school_detail(self, school_id, **kw):
        school = request.env['school_management.school'].search([('id', '=', school_id)])
        return request.render('school_management.school_details_view_portal', {'school': school,
                                                                               'page_name': 'school_details'})


