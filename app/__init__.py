from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import parser_bp
    app.register_blueprint(parser_bp)

    @app.route('/health')
    def health():
        return {"status": "healthy", "service": "cyk-parser-backend"}

    return app