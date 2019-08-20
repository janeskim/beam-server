""" Base model class """
import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BaseModel(Base):
    """ Base model """
    __abstract__ = True
    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False,
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False,
    )

    def __repr__(self):
        fields = {**getattr(self, '__dict__', None)}
        if fields:
            fields.pop('_sa_instance_state', None)
            for key, value in fields.items():
                if isinstance(value, BaseModel):
                    fields[key] = f'{type(value)}(id={value.id} - truncated)'
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, BaseModel):
                            fields[key] = f'{type(value)}(id={item.id} - truncated)'
            return f'{type(self)}{fields}'
        return super().__repr__()
