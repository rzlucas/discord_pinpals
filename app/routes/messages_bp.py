# messages_bp
from flask import Blueprint
from ..controllers.messages_controller import MessagesController

messages_bp = Blueprint('messages_bp', __name__)

messages_bp.route('/', methods=['GET'])(MessagesController.get_all)
messages_bp.route('/<int:ID>', methods=['GET'])(MessagesController.get)
messages_bp.route('/', methods=['POST'])(MessagesController.create)
messages_bp.route('/<int:message_id>', methods=['PUT'])(MessagesController.update)
messages_bp.route('/<int:message_id>', methods=['DELETE'])(MessagesController.delete)
