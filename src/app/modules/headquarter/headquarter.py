from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from interface.headquarter import Headquarter

auth_bp = Blueprint('headquarter', __name__)
# auth_bp.config['JWT_SECRET_KEY'] = 'uptc2025'

# jwt = JWTManager(auth_bp)

headquarters = []


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "empservboy" and password == "1234":

        return "login exitoso para headquarter", 200
    else:
        response = jsonify({"mensaje": "Credenciales incorrectas"})
        return response, 401


@auth_bp.route('/headquarters', methods=['GET'])
# @jwt_required()
def headquartersList():
    return jsonify(headquarters)


@auth_bp.route('/createHeadquarter', methods=['POST'])
# @jwt_required()
def createHeadquarter():
    id = len(headquarters) + 1
    data = request.get_json()
    name = data.get('name')
    state = data.get('state')
    company_id = data.get('company_id')

    newHeadquarter = Headquarter(
        id,
        name,
        state,
        company_id
    )

    headquarters.append(newHeadquarter.to_json())

    return jsonify({"mensaje": "Headquarter creado exitosamente"}), 201


@auth_bp.route('/headquarter/<id>', methods=['GET'])
# @jwt_required()
def headquarterById(id):
    headquarter = next((e for e in headquarters if e['id'] == id), None)

    if headquarter is not None:
        return jsonify(headquarter), 200
    else:
        return jsonify({"mensaje": "Headquarter no encontrado"}), 404


@auth_bp.route('/updateHeadquarter/<id>', methods=['PUT'])
# @jwt_required()
def updateHeadquarter(id):
    data = request.get_json()
    headquarter = next((e for e in headquarters if e['id'] == id), None)

    if headquarter is not None:
        headquarter['name'] = data.get('name', headquarter['name'])
        headquarter['state'] = data.get('state', headquarter['state'])
        headquarter['company_id'] = data.get(
            'company_id', headquarter['company_id'])

        return jsonify({"mensaje": "Headquarter actualizado exitosamente"}), 200
    else:
        return jsonify({"mensaje": "Headquarter no encontrado"}), 404


@auth_bp.route('/deleteHeadquarter/<id>', methods=['DELETE'])
# @jwt_required()
def deleteHeadquarter(id):
    global headquarters
    headquarters = [e for e in headquarters if e['id'] != id]

    return jsonify({"mensaje": "Headquarter eliminado exitosamente"}), 200


if __name__ == '__main__':
    auth_bp.run(host='0.0.0.0', port=5000, debug=True)
