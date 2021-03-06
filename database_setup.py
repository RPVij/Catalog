import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Item(Base):
    __tablename__ = 'item'

    name =  Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    size = Column(String(8))
    category_id = Column(Integer, ForeignKey('category.id'))
    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
    category = relationship(Category, backref=backref("Item", cascade="all, delete"))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'size': self.size,
        }



# engine = create_engine('sqlite:///catalog.db')
engine = create_engine('postgresql://catalog:password@localhost/catalog')

Base.metadata.create_all(engine)
