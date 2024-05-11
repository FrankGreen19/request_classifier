from flask import request, Response
from src.services.prediction_service import get_prediction
from app_init import app
from src.models.models import RequestClass
from src.services.session_maker import db_session


@app.route('/api/message', methods=["POST"])
def message():
    try:
        prediction_class = get_prediction(request.form["message"])
    except:
        prediction_class = None

    if prediction_class is None:
        return {'text': 'Не удалось распознать Ваш запрос. Пожалуйста, перефразируйте и попробуйте еще раз'}, 400
    else:
        result = None
        with db_session() as session:
            r_class = session.query(RequestClass).filter_by(alias=prediction_class).first()
            result = r_class.to_dto().to_json()

    return result, 200
