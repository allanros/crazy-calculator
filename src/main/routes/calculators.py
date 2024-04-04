from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculador_1():
    print(request.get_json())
    return jsonify({'success': True})