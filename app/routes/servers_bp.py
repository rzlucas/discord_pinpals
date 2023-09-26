# servers_bp
from flask import Blueprint
from ..controllers.servers_controller import ServersController

servers_bp = Blueprint('servers_bp', __name__)

servers_bp.route('/', methods=['GET'])(ServersController.get_all)
servers_bp.route('/<int:server_id>', methods=['GET'])(ServersController.get)
servers_bp.route('/', methods=['POST'])(ServersController.create)
servers_bp.route('/<int:server_id>', methods=['PUT'])(ServersController.update)
servers_bp.route('/<int:server_id>', methods=['DELETE'])(ServersController.delete)
