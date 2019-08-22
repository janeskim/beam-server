""" Blueprint for users """
import json

from flask import Blueprint, jsonify, make_response, request
from marshmallow import ValidationError

from src.db import db_session
from src.models.user import User, user_schema, users_schema


bp = Blueprint('users', __name__)


@bp.route('/users')
def index():
    """
    View function to return all users
    """
    users = db_session.query(User).all()
    return (json.dumps(users_schema.dump(users)), 200, {'content_type': 'application/json'})


@bp.route('/users/<int:user_id>')
def get(user_id):
    """
    View function to GET user
    """
    user = db_session.query(User).get(user_id)

    if not user:
        error = "User id {0} doesn't exist.".format(user_id)
        return (json.dumps({'message': error}), 404, {'content-type': 'application/json'})

    return (json.dumps(user_schema.dump(user)), 200, {'content-type': 'application/json'})


@bp.route('/register', methods=['POST'])
def register():
    """
    View function to register new user
    """
    try:
        user = user_schema.load(request.get_json())
        db_session.add(user)
        db_session.commit()
        return (json.dumps(user_schema.dump(user)), 200, {'content-type': 'application/json'})
    except ValidationError as err:
        return make_response(jsonify({'message': err.messages}), 422)
