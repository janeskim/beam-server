""" Config file for environments """
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ Base class for config """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    """ Config class for production """
    DEBUG = False


class StagingConfig(Config):
    """ Config class for staging """
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """ Config class for development """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """ Config class for testing """
    TESTING = True
