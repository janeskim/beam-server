""" User model """
import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from marshmallow import Schema, ValidationError, fields, post_load, validates

from flask_bcrypt import Bcrypt

from src.db import db_session


Base = declarative_base()

class User(Base):
    """ User model """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), nullable=False)
    _password = Column(String(255), nullable=False)

    @property
    def password(self):
        """ Getter for private _password property """
        return self._password

    @password.setter
    def password(self, plaintext):
        """ Setter to hash password property """
        bcrypt = Bcrypt()
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')


class UserSchema(Schema):
    """ User schema to serialize """
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    password = fields.String(load_only=True, required=True)
    email = fields.String(required=True)
    username = fields.String(required=True)

    @validates('email')
    def validates_email_exists(self, data):
        """ Validate uniqueness of email """
        if db_session.query(User).filter_by(email=data).count() > 0:
            raise ValidationError('Email is already registered.')

    @post_load
    def make_object(self, data):
        """ Convert private attribute upon load """
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
