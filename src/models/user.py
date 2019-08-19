""" User model """
import datetime

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

    def __repr__(self):
        return "<User(id='%s', email='%s' username='%s')>" % (self.id, self.email, self.username)

    @property
    def password(self):
        """ Getter for private _password property """
        return self._password

    @password.setter
    def password(self, plaintext):
        """ Setter to hash password property """
        bcrypt = Bcrypt()
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')
