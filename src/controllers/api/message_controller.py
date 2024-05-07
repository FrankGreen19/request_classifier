from flask import request
from src.services.prediction_service import get_prediction
from app_init import app
from src.models.models import RequestClass, session
import json


@app.route('/api/message', methods=["POST"])
def message():
    try:
        prediction_class = get_prediction(request.form["message"])
    except:
        prediction_class = None

    if prediction_class is None:
        result = 'Не удалось распознать Ваш запрос. Пожалуйста, перефразируйте и попробуйте еще раз'
    else:
        r_class = session.query(RequestClass).filter_by(alias=prediction_class).first()
        session.commit()

        result = r_class.to_dto().to_json()

    return result
