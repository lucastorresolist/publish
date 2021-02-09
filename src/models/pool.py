from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Integer
from sqlalchemy.orm import relationship, validates
from src.models.base_model import BaseModel


class Pool(BaseModel):
    __tablename__ = 'pool'

    id_product = Column('fk_product', Integer, ForeignKey('product.id'), 
                        nullable=False)
    id_seller = Column('fk_seller', Integer, ForeignKey('seller.id'), 
                        nullable=False)
    approved = Column('approved', Boolean, nullable=False)