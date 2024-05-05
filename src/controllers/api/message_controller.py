from flask import request
import command
from app_init import app
from services import class_service


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
