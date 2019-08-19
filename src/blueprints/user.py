""" Blueprint to test db config """
import json

from flask import Blueprint

from src.db import db_session
from src.models.user import User


bp = Blueprint('users', __name__)


@bp.route('/users')
def users_index():
    """ View function to return all messages """
    values = db_session.query(User).all()

    results = [{'id': value.id} for value in values]

    return (json.dumps(results), 200, {'content_type': 'application/json'})
