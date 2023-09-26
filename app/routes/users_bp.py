# user_bp
from flask import Blueprint
from ..controllers.users_controller import UsersController

users_bp = Blueprint('users_bp', __name__)

users_bp.route('/', methods=['GET'])(UsersController.get_all)
users_bp.route('/<int:user_id>', methods=['GET'])(UsersController.get)
users_bp.route('/', methods=['POST'])(UsersController.create)
users_bp.route('/<int:user_id>', methods=['PUT'])(UsersController.update)
users_bp.route('/<int:user_id>', methods=['DELETE'])(UsersController.delete)
