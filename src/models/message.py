""" Message model to test db config """
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Message(Base):
    """ Message model """
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message = Column(String)

    def __repr__(self):
        return "<Message(message='%s')>" % (self.message)
