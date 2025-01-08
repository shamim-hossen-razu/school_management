from odoo import http
from odoo.http import request


class SchoolManagement(http.Controller):

    @http.route('/school_management/banner', type='json', auth='user')
    def get_banner(self):
        banner_html = """
        <div class="o_kanban_view_banner" style="background-color: #f8d7da; color: #721c24; padding: 10px; border: 1px solid #f5c6cb; border-radius: 5px; text-align: center; width: 100%; box-sizing: border-box;">
            <span style="font-weight: bold;">Important Notification:</span> School Management System Update
        </div>
        """
        return {'html': banner_html}

    @http.route('/index', auth='none')
    def index(self, **kw):
        # return "Hello, world"

        return """
            <html>
                <head>
                    <title>School Management System</title>
                </head>
                <body>
                    <h1>Welcome to School Management System</h1>
                </body>
            </html>
        """

    @http.route('/school_management/students', auth='public', website=True)
    def students(self, **kw):
        students = request.env['school_management.student'].search([])

        return request.render('school_management.students', {
            'students': students
        })
