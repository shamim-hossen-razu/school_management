from urllib.parse import urlparse
from urllib.parse import urlparse, parse_qs
from odoo.exceptions import AccessError
from odoo import api, http, modules
from odoo.http import request, Response
import jwt
import datetime
from werkzeug.wrappers import Response
import json


class CustomEvent(http.Controller):
    @http.route('/web/api/create_event', type='json', auth="none", cors="*", methods=['POST'])
    def create_event(self, **kw):
        # Example token (replace with your actual token)
        token = http.request.params['jwt']

        # Secret key used to encode the token (must be the same as the one used for encoding)
        secret_key = 'your_secret_key'

        try:
            # Decode the token
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            user_id = decoded_payload['user_id']
            print("User id", user_id)

            # Check if the user has permission to create the event
            env = request.env(user=user_id)
            model = env['custom.event']

            # Check access rights
            try:
                user_has_access = model.check_access_rights('create', raise_exception=True)
                print("User has access", user_has_access)
            except AccessError as e:
                return {'success': False, 'error': 'Access denied: ' + str(e)}
            if user_has_access:
                event = model.create({
                    'name': kw.get('name'),
                    'location': kw.get('location'),
                    'date': kw.get('date')
                })
                return {'event_id': event.id, 'message': 'Event created successfully',
                        'success': True}

        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
        except AccessError as e:
            return {'error': 'Access denied: ' + str(e)}
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}

    @http.route('/web/api/delete_event', type='json', auth="none", cors="*", csrf=False, methods=['POST'])
    def delete_event(self, **kw):
        # Check the CORS headers
        token = http.request.params['jwt']

        # Secret key used to encode the token (must be the same as the one used for encoding)
        secret_key = 'your_secret_key'

        try:
            # Decode the token
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            user_id = decoded_payload['user_id']

            # Check if the user has permission to delete the event
            env = request.env(user=user_id)
            model = env['custom.event']

            # Check access rights
            try:
                user_has_access = model.check_access_rights('unlink', raise_exception=True)
            except AccessError as e:
                print('No access to delete')
                return {'success': False, 'error': 'Access denied: ' + str(e)}
            if user_has_access:
                event = model.search([('id', '=', (int(kw.get('id'))))])
                if event:
                    event.unlink()
                    return {'success': True, 'message': 'Event deleted successfully'}
                else:
                    return {'error': 'Event not found'}

        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
        except AccessError as e:
            return {'error': 'Access denied: ' + str(e)}
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}

    @http.route('/web/api/update_event', type='json', auth="none", cors="*", methods=['POST'])
    def update_event(self, **kw):
        # Example token (replace with your actual token)
        token = http.request.params['jwt']

        # Secret key used to encode the token (must be the same as the one used for encoding)
        secret_key = 'your_secret_key'

        try:
            # Decode the token
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            user_id = decoded_payload['user_id']

            # Check if the user has permission to update the event
            env = request.env(user=user_id)
            model = env['custom.event']

            # Check access rights
            try:
                user_has_access = model.check_access_rights('write', raise_exception=True)
            except AccessError as e:
                return {'error': 'Access denied: ' + str(e)}
            if user_has_access:
                event = model.search([('id', '=', int(kw.get('id')))])
                if not event:
                    return {'error': 'Event not found'}
                event.write({
                    'name': kw.get('name'),
                    'location': kw.get('location'),
                    'date': kw.get('date')
                })
                return {'message': 'Event updated successfully'}

        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
        except AccessError as e:
            return {'error': 'Access denied: ' + str(e)}
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}

    @http.route('/web/api/events/<id>', type='json', auth="none", methods=['GET', 'PUT', 'DELETE'])
    def read_update_delete_event(self, **kw):
        # Example token (replace with your actual token)
        token = http.request.params['jwt']

        # Secret key used to encode the token (must be the same as the one used for encoding)
        secret_key = 'your_secret_key'

        try:
            # Decode the token
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            user_id = decoded_payload['user_id']

            # Check if the user has permission to read the event
            env = request.env(user=user_id)
            model = env['custom.event']

            # Check access rights
            try:
                user_has_read_access = model.check_access_rights('read', raise_exception=True)
                user_has_write_access = model.check_access_rights('write', raise_exception=True)
                user_has_unlink_access = model.check_access_rights('unlink', raise_exception=True)
            except AccessError as e:
                return {'error': 'Access denied: ' + str(e)}
            if request.httprequest.method == 'GET' and user_has_read_access:
                event = model.browse(int(kw.get('id')))
                return {
                    'name': event.name,
                    'location': event.location,
                    'date': event.date
                }
            elif request.httprequest.method == 'PUT' and user_has_write_access:
                event = model.browse(int(kw.get('id')))
                event.write({
                    'name': kw.get('name'),
                    'location': kw.get('location'),
                    'date': kw.get('date')
                })
                return {'message': 'Event updated successfully'}
            elif request.httprequest.method == 'DELETE' and user_has_unlink_access:
                event = model.search([('id', '=', (int(kw.get('id'))))])
                if event:
                    event.unlink()
                    return {'message': 'Event deleted successfully'}
                else:
                    return {'error': 'Event not found'}

        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
        except AccessError as e:
            return {'error': 'Access denied: ' + str(e)}
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}

    @http.route('/web/api/events', type='json', auth="public")
    def list_events(self, **kw):
        events = request.env['custom.event'].search([('date', '>', datetime.datetime.now())])
        event_list = [{'id': event.id, 'name': event.name, 'location': event.location, 'date': event.date} for event in
                      events]
        return {'events': event_list}

    @http.route('/web/api/fetch_events', type='json', auth="none", cors="*", methods=['POST'])
    def paginated_read(self, **kw):
        secret_key = 'your_secret_key'

        try:
            # Retrieve and validate the JWT token
            token = http.request.params.get('jwt')
            page_number = http.request.params.get('page_number', 1)
            page_size = http.request.params.get('page_size', 5)
            if not token:
                return {'error': 'JWT token is missing'}

            try:
                decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return {'error': 'Token has expired'}
            except jwt.InvalidTokenError:
                return {'error': 'Invalid token'}

            user_id = decoded_payload.get('user_id')
            if not user_id:
                return {'error': 'User ID is missing from the token'}

            # Access the environment as the specified user
            env = request.env(user=user_id)
            model = env['custom.event']

            # Check user access rights
            try:
                model.check_access_rights('read', raise_exception=True)
            except AccessError:
                return {'error': 'Access denied: You do not have permission to view events'}

            # Retrieve paginated events
            events = model.search([], limit=page_size, offset=(page_number - 1) * page_size)
            event_list = [{'id': event.id, 'name': event.name, 'location': event.location, 'date': event.date} for event
                          in events]

            return {
                'page_number': page_number,
                'page_size': page_size,
                'total_events': model.search_count([]),
                'events': event_list
            }

        except Exception as e:
            return {'error': f'An unexpected error occurred: {str(e)}'}

    @http.route('/web/api/read_event', type='json', auth="none", cors='*', methods=['GET'])
    def read_event(self, **kw):
        # Example token (replace with your actual token)
        token = http.request.params['jwt']

        # Secret key used to encode the token (must be the same as the one used for encoding)
        secret_key = 'your_secret_key'

        try:
            # Decode the token
            decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            user_id = decoded_payload['user_id']

            # Check if the user has permission to read the event
            env = request.env(user=user_id)
            model = env['custom.event']

            # Check access rights
            try:
                user_has_read_access = model.check_access_rights('read', raise_exception=True)
            except AccessError as e:
                return {'error': 'Access denied: ' + str(e)}
            if user_has_read_access:
                event = model.search([('id', '=', int(kw.get('id')))])
                if not event:
                    return {'error': 'Event not found'}
                return {
                    'id': event.id,
                    'name': event.name,
                    'location': event.location,
                    'date': event.date
                }

        except jwt.ExpiredSignatureError:
            return {'error': 'Token has expired'}
        except jwt.InvalidTokenError:
            return {'error': 'Invalid token'}
        except AccessError as e:
            return {'error': 'Access denied: ' + str(e)}
        except Exception as e:
            return {'error': 'An error occurred: ' + str(e)}

