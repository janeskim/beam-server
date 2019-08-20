""" User model """
import datetime

from marshmallow import fields, post_load, Schema
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from flask_bcrypt import Bcrypt


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
    email = fields.String()
    username = fields.String()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
