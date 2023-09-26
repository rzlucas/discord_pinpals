# servers_controller
from flask import request, current_app

from .. import Servers
from ..models.exceptions import ServerNotFound


class ServersController:
    @classmethod
    def get(cls, server_id):
        server = Servers(ID=server_id)
        result = Servers.get(server)
        if result is not None:
            return result.serialize(), 200
        else:
            raise ServerNotFound(server_id)


    @classmethod
    def get_all(cls):
        Servers = current_app.config['Servers']
        server_objects = Servers.get_all()
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200

    @classmethod
    def create(cls):
        Servers = current_app.config['Servers']
        data = request.json
        server = Servers(**data)
        Servers.create(server)
        return {'message': 'Server created successfully'}, 201

    @classmethod
    def update(cls, ID):
        Servers = current_app.config['Servers']
        data = request.json
        data['ID'] = ID
        server = Servers(**data)
        Servers.update(server)
        return {'message': 'Server updated successfully'}, 200

    @classmethod
    def delete(cls, ID):
        Servers = current_app.config['Servers']
        server = Servers(ID=ID)
        Servers.delete(server)
        return {'message': 'Server deleted successfully'}, 204
