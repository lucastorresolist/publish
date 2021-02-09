from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, validates
from src.models.base_model import BaseModel


class PoolModel(BaseModel):
    __tablename__ = 'pool'

    id_channel = Column('id_channel', Integer, ForeignKey('channel.id'), 
                        nullable=False, lazy='subquery')