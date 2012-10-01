from sqlalchemy import Column, Integer, String, Numeric, Boolean, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref
from flask_website.utils import sqlite
from flask_website.data.database import Base

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    short_description = Column(String(512))
    image_url = Column(String(120))
    price = Column(String()) #FIXME: Figure out better type here...
    stock = Column(Integer)
    color_id = Column(Integer, ForeignKey('color.id'))
    color = relationship("Color", backref=backref("parent", uselist=False))
    introduction_date = Column(Date)
    discontinued = Column(Boolean)
    product_images = relationship("ProductImage", back_populates="product")

    def __init__(self):
	pass

    def __unicode__(self):
        return self.name
