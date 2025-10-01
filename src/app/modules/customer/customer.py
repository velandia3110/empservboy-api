from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from interface.customer import Customer

auth_bp = Blueprint('customer', __name__)
#auth_bp.config['JWT_SECRET_KEY'] = 'uptc2025'  

#jwt = JWTManager(auth_bp)

customers = []


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "empservboy" and password == "1234":
       
        return "login exitoso", 200
    else:
        response = jsonify({"mensaje": "Credenciales incorrectas"})
        return response, 401


@auth_bp.route('/customers', methods=['GET'])
#@jwt_required()
def customersList():
    return jsonify(customers)


@auth_bp.route('/createCustomer', methods=['POST'])
#@jwt_required()
def createCustomer():
    id = len(customers) + 1
    data = request.get_json()
    nit = data.get('nit')
    name = data.get('name')
    telephone = data.get('telephone')
    representative = data.get('representative')
    representative_role = data.get('representative_role')
    email = data.get('email')
    complementary_direction = data.get('complementary_direction')
    state = data.get('state')
    image = data.get('image')
    municipios_id = data.get('municipios_id')

    newCustomer = Customer(
        id,
        nit,
        name,
        telephone,
        representative,
        representative_role,
        email,
        complementary_direction,
        state,
        image,
        municipios_id
    )

    customers.append(newCustomer.to_json())

    return jsonify({"mensaje": "Cliente creado exitosamente"}), 201


@auth_bp.route('/customer/<id>', methods=['GET'])
#@jwt_required()
def customerById(id):
    customer = next((e for e in customers if e['id'] == id), None)

    if customer is not None:
        return jsonify(customer), 200
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404


@auth_bp.route('/updateCustomer/<id>', methods=['PUT'])
#@jwt_required()
def updateCustomer(id):
    data = request.get_json()
    customer = next((e for e in customers if e['id'] == id), None)

    if customer is not None:
        customer['nit'] = data.get('nit', customer['nit'])
        customer['name'] = data.get('name', customer['name'])
        customer['telephone'] = data.get('telephone', customer['telephone'])
        customer['representative'] = data.get('representative', customer['representative'])
        customer['representative_role'] = data.get('representative_role', customer['representative_role'])
        customer['email'] = data.get('email', customer['email'])
        customer['complementary_direction'] = data.get('complementary_direction', customer['complementary_direction'])
        customer['state'] = data.get('state', customer['state'])
        customer['image'] = data.get('image', customer['image'])
        customer['municipios_id'] = data.get('municipios_id', customer['municipios_id'])

        return jsonify({"mensaje": "Cliente actualizado exitosamente"}), 200
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404


@auth_bp.route('/deleteCustomer/<id>', methods=['DELETE'])
#@jwt_required()
def deleteCustomer(id):
    global customers
    customers = [e for e in customers if e['id'] != id]

    return jsonify({"mensaje": "Cliente eliminado exitosamente"}), 200


if __name__ == '__main__':
    auth_bp.run(host='0.0.0.0', port=5000, debug=True)
