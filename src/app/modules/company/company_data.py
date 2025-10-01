from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from interface.company import Company

auth_bp = Blueprint('company', __name__)
# auth_bp.config['JWT_SECRET_KEY'] = 'uptc2025'

# jwt = JWTManager(auth_bp)

companies = []


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "empservboy" and password == "1234":

        return "login exitoso para empresa", 200
    else:
        response = jsonify({"mensaje": "Credenciales incorrectas"})
        return response, 401


@auth_bp.route('/companies', methods=['GET'])
# @jwt_required()
def companiesList():
    return jsonify(companies)


@auth_bp.route('/createCompany', methods=['POST'])
# @jwt_required()
def createCompany():
    id = len(companies) + 1
    data = request.get_json()
    nit = data.get('nit')
    telephone = data.get('telephone')
    direction = data.get('direction')
    business_name = data.get('business_name')
    email = data.get('email')
    image = data.get('image')

    newCompany = Company(
        id,
        nit,
        telephone,
        direction,
        business_name,
        email,
        image
    )

    companies.append(newCompany.to_json())

    return jsonify({"mensaje": "Empresa creada exitosamente"}), 201


@auth_bp.route('/company/<id>', methods=['GET'])
# @jwt_required()
def companyById(id):
    company = next((e for e in companies if e['id'] == id), None)

    if company is not None:
        return jsonify(company), 200
    else:
        return jsonify({"mensaje": "Empresa no encontrada"}), 404


@auth_bp.route('/updateCompany/<id>', methods=['PUT'])
# @jwt_required()
def updateCompany(id):
    data = request.get_json()
    company = next((e for e in companies if e['id'] == id), None)

    if company is not None:
        company['nit'] = data.get('nit', company['nit'])
        company['telephone'] = data.get('telephone', company['telephone'])
        company['direction'] = data.get('direction', company['direction'])
        company['business_name'] = data.get(
            'business_name', company['business_name'])
        company['email'] = data.get('email', company['email'])
        company['image'] = data.get('image', company['image'])

        return jsonify({"mensaje": "Empresa actualizada exitosamente"}), 200
    else:
        return jsonify({"mensaje": "Empresa no encontrada"}), 404


@auth_bp.route('/deleteCompany/<id>', methods=['DELETE'])
# @jwt_required()
def deleteCompany(id):
    global companies
    companies = [e for e in companies if e['id'] != id]

    return jsonify({"mensaje": "Empresa eliminada exitosamente"}), 200


if __name__ == '__main__':
    auth_bp.run(host='0.0.0.0', port=5000, debug=True)
