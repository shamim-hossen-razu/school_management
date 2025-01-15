from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.http import request
from odoo import http, _


class MySchoolPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(MySchoolPortal, self)._prepare_home_portal_values(counters)
        values['school_count'] = request.env['school_management.school'].search_count([])
        print("values: ", values)
        return values

    @http.route(['/my/school', '/my/school/page/<int:page>'], type='http', auth='user', website=True)
    def my_school_list(self, page=1, sortby=None, search=None, search_in='all', **kw):
        # add sort by feature
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
            'established_date': {'label': _('Establish Date'), 'order': 'established_date'},
        }
        if not search_in:
            search_in = 'name'
        search_list = {
            'all': {'label': _('All'), 'input': 'all', 'domain': []},
            'name': {'label': _('Name'), 'input': 'name', 'domain': [('name', 'ilike', search)]}
        }
        search_domain = search_list[search_in]['domain']
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']
        school_count = request.env['school_management.school'].search_count([])
        pager = portal_pager(url='/my/school',
                                      total=school_count,
                                      page=page, step=5,
                                      scope=5,
                                      url_args={'sortby': sortby, 'search_in': search_in, 'search': search})
        schools = request.env['school_management.school'].search(search_domain, limit=5, offset=pager['offset'], order=order)
        return request.render('school_management.school_list_view_template', {
            'schools': schools,
            'page_name': 'my_school',
            'pager': pager,
            'sortby': sortby,
            'searchbar_sortings': searchbar_sortings,
            'searchbar_inputs': search_list,
            'search_in': search_in,
            'search': search,
        })

    @http.route(['/my/school/<int:school_id>'], type='http', auth='user', website=True)
    def my_school_detail(self, school_id, **kw):
        # get id of prev and next school of current school
        school_ids = request.env['school_management.school'].search([]).ids
        school_index = school_ids.index(school_id)
        school_count = len(school_ids)
        prev_school_id = school_ids[school_index - 1] if school_index > 0 else False
        next_school_id = school_ids[school_index + 1] if school_index < school_count - 1 else False

        school = request.env['school_management.school'].search([('id', '=', school_id)])
        return request.render('school_management.school_details_view_portal', {'school': school,
                                                                               'page_name': 'school_details',
                                                                               'prev_record': f'/my/school/{prev_school_id}' if prev_school_id else False,
                                                                               'next_record': f'/my/school/{next_school_id}' if next_school_id else False})
