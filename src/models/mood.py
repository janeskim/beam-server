""" Mood model """
from sqlalchemy import event, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from marshmallow import (
    Schema,
    ValidationError,
    fields,
    pre_dump,
    post_load,
    validates,
    validates_schema
)

from src.db import db_session
from src.models.base_model import BaseModel
from src.models.color import Color
from src.models.user import User


class Mood(BaseModel):
    """ Mood model class """
    __tablename__ = 'moods'
    color_hex = Column(String, nullable=False)
    mood_at = Column(DateTime, nullable=False)
    name = Column(String, nullable=False)
    notes = Column(String)
    color_id = Column(Integer, ForeignKey('colors.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    color = relationship('Color', foreign_keys=[color_id], uselist=False)
    user = relationship('User', foreign_keys=[user_id], uselist=False)


def after_insert_listener(mapper, connection, target):
    """ Set mood_at using created_at if none exists """
    if not target.mood_at:
        target.mood_at = target.created_at

event.listen(Mood, 'after_insert', after_insert_listener)


class MoodSchema(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    mood_at = fields.DateTime()
    name = fields.String(required=True)
    notes = fields.String()
    color_hex = fields.String()
    color_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)

    @validates('user_id')
    def validates_user_id(self, data):
        """ Validate existence of user """
        if not db_session.query(User).get(data):
            raise ValidationError('User does not exist.')

    @validates('color_id')
    def validates_color_id(self, data):
        """ Validate existence of color """
        if not db_session.query(Color).get(data):
            raise ValidationError('Color does not exist.')

    @post_load
    def make_object(self, data, **kwargs):
        """ Load mood object """
        return Mood(**data)


mood_schema = MoodSchema()
moods_schema = MoodSchema(many=True)
