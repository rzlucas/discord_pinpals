# messages_controller.py
from flask import request

from ..models.exceptions import MessageNotFound
from ..models.messages import Messages


class MessagesController:
    @classmethod
    def get(cls, ID):
        message = Messages(ID=ID)
        result = Messages.get(message)
        if result is not None:
            return result.serialize(), 200
        else:
            raise MessageNotFound(ID)

    @classmethod
    def get_all(cls):
        message_objects = Messages.get_all()
        messages = []
        for message in message_objects:
            messages.append(message.serialize())
        return messages, 200

    @classmethod
    def create(cls):
        data = request.json
        message = Messages(**data)
        Messages.create(message)
        return {'message': 'Message created successfully'}, 201

    @classmethod
    def update(cls, ID):
        data = request.json
        data['ID'] = ID
        message = Messages(**data)
        Messages.update(message)
        return {'message': 'Message updated successfully'}, 200

    @classmethod
    def delete(cls, ID):
        message = Messages(ID=ID)
        Messages.delete(message)
        return {'message': 'Message deleted successfully'}, 204
