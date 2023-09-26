# exception
from flask import jsonify


class UserNotFound(Exception):
    def __init__(self, user_id):
        super().__init__()
        self.description = f"User with id {user_id} not found"
        self.status_code = 404
        self.name = "User Not Found"

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class ServerNotFound(Exception):
    def __init__(self, server_id):
        super().__init__()
        self.description = f"Server with id {server_id} not found"
        self.status_code = 404
        self.name = "Server Not Found"

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class MessageNotFound(Exception):
    def __init__(self, message_id):
        super().__init__()
        self.description = f"Message with id {message_id} not found"
        self.status_code = 404
        self.name = "Message Not Found"

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response


class ChannelNotFound(Exception):
    def __init__(self, channel_id):
        super().__init__()
        self.description = f"Channel with id {channel_id} not found"
        self.status_code = 404
        self.name = "Channel Not Found"

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
