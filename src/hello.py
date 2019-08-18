""" Blueprint to test db config """
import json

from flask import Blueprint

from src.db import db_session
from src.models.message import Message


hello_blueprint = Blueprint('hello', __name__)


@hello_blueprint.route('/messages')
def messages():
    """ View function to return all messages """
    values = db_session.query(Message).all()

    results = [{'message': value.message} for value in values]

    return (json.dumps(results), 200, {'content_type': 'application/json'})
