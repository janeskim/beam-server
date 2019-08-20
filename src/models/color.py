""" Color model """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from marshmallow import (
    Schema, ValidationError, fields, post_load, validates, validates_schema
)

from src.db import db_session
from src.models.base_model import BaseModel
from src.models.user import User


class Color(BaseModel):
    """ Color model """
    __tablename__ = 'colors'
    hex_code = Column(String, nullable=False)
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    user = relationship('User', foreign_keys=[user_id], uselist=False)


class ColorSchema(Schema):
    """ Color schema to serialize """
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    hex_code = fields.String(required=True)
    user_id = fields.Integer(required=True)

    @validates('user_id')
    def validates_user_id(self, data):
        """ Validate existence of user """
        if not db_session.query(User).get(data):
            raise ValidationError('User does not exist.')

    @validates_schema
    def validates_colors_schema(self, data, **kwargs):
        """ Validate that hex code is unique by user """
        hex_code = data.get('hex_code')
        user_id = data.get('user_id')
        if db_session.query(Color).filter_by(user_id=user_id, hex_code=hex_code).count() > 0:
            raise ValidationError(
                'Hex code {0} already exists for user {1}'.format(hex_code, user_id)
            )

    @post_load
    def make_object(self, data, **kwargs):
        """ Load color object """
        return Color(**data)


color_schema = ColorSchema()
colors_schema = ColorSchema(many=True)
