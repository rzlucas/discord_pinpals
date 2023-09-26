# users_controller.py
from flask import request

from ..models.exceptions import UserNotFound
from ..models.users import Users


class UsersController:
    @classmethod
    def get(cls, user_id):
        user = Users(ID=user_id)
        result = Users.get(user)
        if result is not None:
            return result.serialize(), 200
        else:
            raise UserNotFound(user_id)

    @classmethod
    def get_all(cls):
        user_objects = Users.get_all()
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200

    @classmethod
    def create(cls):
        data = request.json
        user = Users(**data)
        Users.create(user)
        return {'message': 'User created successfully'}, 201

    @classmethod
    def update(cls, ID):
        data = request.json
        data['ID'] = ID
        user = Users(**data)
        Users.update(user)
        return {'message': 'User updated successfully'}, 200

    @classmethod
    def delete(cls, ID):
        user = Users(ID=ID)
        Users.delete(user)
        return {'message': 'User deleted successfully'}, 204
