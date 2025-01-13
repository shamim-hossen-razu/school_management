from odoo import http
from odoo import api, http, modules
from odoo.http import request, Response
import jwt
import datetime

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

    class CustomAuth(http.Controller):
        @http.route('/web/api/signin', type='json', auth="none", csrf=False, website=False, cors='*', methods=['POST'])
        def signin(self, **kw):
            try:
                # Attempt to authenticate the user
                user_id = request.session.authenticate("odoo-16", request.params['login'],
                                                       request.params['password'])

                if not user_id:
                    return {'success': False, 'message': 'Authentication failed: Invalid login or password.'}

                # Create JWT token
                payload = {
                    'user_id': user_id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=240)  # Token expiration time
                }
                secret_key = 'your_secret_key'  # Replace with your actual secret key
                token = jwt.encode(payload, secret_key, algorithm='HS256')

                return {
                    'success': True,
                    'message': 'Sign in successful!',
                    'id': user_id,
                    'result': {
                        'token': token
                    }
                }

            except Exception as e:
                # In case of an error, return a message
                return {'success': False, 'message': str(e)}