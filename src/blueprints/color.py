""" Blueprint for colors """
import json

from flask import Blueprint, jsonify, make_response, request
from marshmallow import ValidationError

from src.db import db_session
from src.models.color import Color, color_schema, colors_schema


bp = Blueprint('colors', __name__)


@bp.route('/users/<int:user_id>/colors', methods=['GET', 'POST'])
def user_colors(user_id):
    """ View function to retrieve colors by user. """
    if request.method == 'GET':
        colors = db_session.query(Color).filter_by(user_id=user_id).all()
        return (json.dumps(colors_schema.dump(colors)), 200, {'content_type': 'application/json'})

    try:
        data = request.get_json()
        data['user_id'] = user_id
        color = color_schema.load(data)
        db_session.add(color)
        db_session.commit()
        return (json.dumps(color_schema.dump(color)), 200, {'content-type': 'application/json'})
    except ValidationError as err:
        return make_response(jsonify({'message': err.messages}), 422)


@bp.route('/users/<int:user_id>/colors/<int:color_id>', methods=['GET'])
def get_user_color(user_id, color_id):
    """ View function to retrieve color by user. """
    color = db_session.query(Color).filter_by(id=color_id, user_id=user_id).first()

    if not color:
        error = "Color id {0} doesn't exist.".format(color_id)
        return (json.dumps({'message': error}), 404, {'content-type': 'application/json'})

    return (json.dumps(color_schema.dump(color)), 200, {'content-type': 'application/json'})
