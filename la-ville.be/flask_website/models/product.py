from sqlalchemy import Column, Integer, String, Numeric
from flask_website.data.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image_url = Column(String(120))
    price = Column(Numeric())

    def __init__(self, name=None, image_url=None, price=0):
        self.name = name
        self.image_url = image_url
	self.price = price

    def __repr__(self):
        return '<Product %r>' % (self.name)
