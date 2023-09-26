# channels_controller.py
from flask import request

from ..models.channels import Channels
from ..models.exceptions import ChannelNotFound


class ChannelsController:
    @classmethod
    def get(cls, ID):
        channel = Channels(ID=ID)
        result = Channels.get(channel)
        if result is not None:
            return result.serialize(), 200
        else:
            raise ChannelNotFound(ID)

    @classmethod
    def get_all(cls):
        channel_objects = Channels.get_all()
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200

    @classmethod
    def create(cls):
        data = request.json
        channel = Channels(**data)
        Channels.create(channel)
        return {'message': 'Channel created successfully'}, 201

    @classmethod
    def update(cls, ID):
        data = request.json
        data['ID'] = ID
        channel = Channels(**data)
        Channels.update(channel)
        return {'message': 'Channel updated successfully'}, 200

    @classmethod
    def delete(cls, channel_id):
        channel = Channels(ID=channel_id)
        Channels.delete(channel)
        return {'message': 'Channel deleted successfully'}, 204
