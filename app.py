from flask import Flask
from flask_cors import CORS
from api.routes import api_bp

app = Flask(__name__)
CORS(app)

# Registra el blueprint SIN prefijo para que '/' y '/predict' estén disponibles directamente
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
