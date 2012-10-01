from sqlalchemy import Table, Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, backref
from flask_website.utils import sqlite
from flask_website.data.database import Base

association_table = Table('product2productgroup', Base.metadata,
    Column('productgroup_id', Integer, ForeignKey('productgroup.id')),
    Column('product_id', Integer, ForeignKey('product.id'))
)

class ProductGroup(Base):
    __tablename__ = 'productgroup'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    products = relationship("Product",
                    secondary=association_table)

    def __init__(self):
	pass

    def __unicode__(self):
        return self.name
