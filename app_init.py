from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDKFJSDFOWEIOF'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})