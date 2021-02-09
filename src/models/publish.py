from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Integer
from sqlalchemy.orm import relationship, validates
from src.models.base_model import BaseModel
from src.models.channel import Channel
from src.models.pool import Pool


class Publish(BaseModel):
    __tablename__ = 'publish'

    id_pool = Column('id_pool', Integer, ForeignKey('pool.id'), 
                        nullable=False)
    pool = relationship('Pool', foreign_keys=[id_pool],  lazy='subquery')
    id_channel = Column('id_channel', Integer, ForeignKey('channels.id'), 
                        nullable=False)
    channel = relationship('Channel', foreign_keys=[id_channel],  lazy='subquery')
    initial_date = Column('initial_date', DateTime, nullable=False)
    final_date = Column('final_date', DateTime, nullable=True)
    is_activate = Column('is_activate', Boolean, default=False, nullable=False)

    def __init__(self, id_pool:int, id_channel:int,
                 initial_date:datetime, final_date:datetime, is_activate:Boolean = False) -> None:
        self.id_pool = id_pool
        self.id_channel = id_channel
        self.initial_date = datetime.strptime(initial_date, '%d-%m-%Y %H:%M:%S').date()
        self.final_date = datetime.strptime(final_date, '%d-%m-%Y %H:%M:%S').date()
        self.is_activate = is_activate

    @validates('id_pool')
    def id_pool_validation(self, key, id_pool):
        if not isinstance(id_pool, int):
            raise TypeError('id_pool is not int')
        return id_pool

    @validates('id_chennel')
    def id_chennel_validate(self, key, id_chennel):
        if not isinstance(id_chennel, int):
            raise TypeError('initial_date is not int')
        return id_chennel

    @validates('initial_date')
    def initial_date_validation(self, key, initial_date):
        print(initial_date, type(initial_date), datetime.now())
        if not isinstance(initial_date, datetime.date()):
            raise TypeError('initial_date is not datetime')
        if initial_date < datetime.now().date():
            raise ValueError('initial_date is invalid date')
        return initial_date

    @validates('final_date')
    def final_date_validation(self, key, final_date):
        if final_date < self.initial_date:
            raise ValueError('initial_date cannot be after the final_date')
        return final_date

    @validates('is_activate')
    def is_activate_validation(self, key, is_activate):
        if datetime.now().date()>=self.initial_date and (datetime.now().date()<=self.final_date or self.final_date is None):
            is_activate = True
        return is_activate
