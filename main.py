from flask import Flask
from src.app.modules.customer.customer import auth_bp as customer_bp
from src.app.modules.company.company_data import auth_bp as company_bp
from src.app.modules.headquarter.headquarter import auth_bp as headquarter_bp


def create_app():
    app = Flask(__name__)

    # Registro de los blueprints (módulos de rutas)
    app.register_blueprint(customer_bp, url_prefix="/customer")
    app.register_blueprint(company_bp, url_prefix="/company")
    app.register_blueprint(headquarter_bp, url_prefix="/headquarter")
    # app.register_blueprint(products_bp, url_prefix="/products")

    @app.route("/")
    def index():
        return {"message": "API funcionando 🚀"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
