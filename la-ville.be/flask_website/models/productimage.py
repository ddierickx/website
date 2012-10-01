from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_website.utils import sqlite
from flask_website.data.database import Base

class ProductImage(Base):
    __tablename__ = 'productimage'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    image_url = Column(String(120))
    product = relationship("Product", back_populates="product_images")

    def __init__(self, image_url ):
	self.image_url = image_url

    def __repr__(self):
        return '<ProductImage %r>' % (self.image_url)
