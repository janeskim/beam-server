""" Blueprint to test db config """
import json

from flask import Blueprint, request

from src.db import db_session
from src.models.user import User


bp = Blueprint('users', __name__)


@bp.route('/users')
def index():
    """
    View function to return all users
    """
    users = db_session.query(User).all()

    results = [{'id': value.id} for value in users]

    return (json.dumps(results), 200, {'content_type': 'application/json'})


@bp.route('/users/<int:user_id>')
def get(user_id):
    """
    View function to GET user
    """
    user = db_session.query(User).get(user_id)

    if user is None:
        error = "User id {0} doesn't exist.".format(user_id)
        return (json.dumps(error), 404, {'content-type': 'application/json'})

    return (json.dumps(user), 200, {'content-type': 'application/json'})


@bp.route('/register', methods=['POST'])
def register():
    """
    View function to register new user
    """
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    error = None

    if not email:
        error = "Email is required."
    elif not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."
    elif len(db_session.query(User).filter_by(email=email).all()) > 0:
        error = 'User {} is already registered.'.format(email)

    if error is None:
        user = User(username=username, email=email, password=password)
        db_session.add(user)
        db_session.commit()
        return (json.dumps(user), 200, {'content-type': 'application/json'})

    return (json.dumps(error), 403, {'content-type': 'application/json'})
