from sqlalchemy import Column, Integer, String, Numeric, Boolean
from flask_website.utils import sqlite
from flask_website.data.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    short_description = Column(String(512))
    image_url = Column(String(120))
    price = Column(sqlite.SqliteNumeric())
    stock = Column(Integer)
    color = Column(String(32))
    discontinued = Column(Boolean)

    def __init__(self, name, short_description, image_url, price, stock, color, discontinued):
        self.name = name
	self.short_description = short_description
        self.image_url = image_url
	self.price = price
	self.stock = stock
	self.color = color
	self.discontinued = discontinued

    def __repr__(self):
        return '<Product %r>' % (self.name)
