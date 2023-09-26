# error_handlers.bp
from flask import Blueprint
from app.models.exceptions import UserNotFound, ServerNotFound, ChannelNotFound, MessageNotFound

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(UserNotFound)
def handle_user_not_found(error):
    return error.get_response(), error.status_code


@errors.app_errorhandler(ServerNotFound)
def handle_server_not_found(error):
    return error.get_response(), error.status_code


@errors.app_errorhandler(ChannelNotFound)
def handle_channel_not_found(error):
    return error.get_response(), error.status_code


@errors.app_errorhandler(MessageNotFound)
def handle_message_not_found(error):
    return error.get_response(), error.status_code
