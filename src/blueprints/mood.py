""" Blueprints for moods """
import json

from flask import Blueprint, jsonify, make_response, request
from marshmallow import ValidationError

from src.db import db_session
from src.models.color import Color
from src.models.mood import Mood, mood_schema, moods_schema


bp = Blueprint('moods', __name__)


@bp.route('/users/<int:user_id>/moods', methods=['GET', 'POST'])
def user_moods(user_id):
    """ View function to retrieve moods by user. """
    if request.method == 'GET':
        moods = db_session.query(Mood).filter_by(user_id=user_id).all()
        return (json.dumps(moods_schema.dump(moods)), 200, {'content_type': 'application/json'})

    try:
        data = request.get_json()
        color = db_session.query(Color).get(data['color_id'])
        data['user_id'] = user_id
        data['color_hex'] = color.hex_code
        mood = mood_schema.load(data)
        db_session.add(mood)
        db_session.commit()
        return (json.dumps(mood_schema.dump(mood)), 200, {'content-type': 'application/json'})
    except ValidationError as err:
        return make_response(jsonify({'message': err.messages}), 422)


@bp.route('/users/<int:user_id>/moods/<int:mood_id>', methods=['GET'])
def get_user_mood(user_id, mood_id):
    """ View function to retrieve mood by user. """
    mood = db_session.query(Mood).filter_by(id=mood_id, user_id=user_id).first()

    if not mood:
        error = "Mood id {0} doesn't exist.".format(mood_id)
        return (json.dumps({'message': error}), 404, {'content-type': 'application/json'})

    return (json.dumps(mood_schema.dump(mood)), 200, {'content-type': 'application/json'})
