""" App module for Heroku """
import os

from src import create_app
from src.db import db_session
from src.blueprints import user


app = create_app()

app.register_blueprint(user.bp)

# app.config.from_object(os.environ.get('APP_SETTINGS', "config.DevelopmentConfig"))
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Callback function to be called when current application context
    is torn down. Happens after each request to release resources
    used by sesion after each request.
    """
    db_session.remove()
