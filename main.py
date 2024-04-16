from flask import Flask, request, render_template
from flask_cors import CORS

import command
from services import class_service

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDKFJSDFOWEIOF'

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('room.html')


@app.route('/api/message', methods=["POST"])
def message():
    try:
        prediction_class = command.get_prediction(request.form["message"])
    except:
        prediction_class = None

    result = None
    if prediction_class is None:
        result = 'Не удалось распознать Ваш запрос. Пожалуйста, перефразируйте и попробуйте еще раз'
    else:
        result = class_service.classes_data[prediction_class]

    return result
