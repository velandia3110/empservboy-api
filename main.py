from flask import Flask
from src.app.modules.customer.customer import auth_bp

def create_app():
    app = Flask(__name__)

    # Registro de los blueprints (módulos de rutas)
    app.register_blueprint(auth_bp, url_prefix="/customer")
    #app.register_blueprint(users_bp, url_prefix="/users")
    #app.register_blueprint(products_bp, url_prefix="/products")

    @app.route("/")
    def index():
        return {"message": "API funcionando 🚀"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
