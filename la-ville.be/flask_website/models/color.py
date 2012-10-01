from sqlalchemy import Column, Integer, String
from flask_website.data.database import Base

class Color(Base):
    __tablename__ = 'color'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    hexcode = Column(String(7))

    def __init__(self):
	pass

    def __unicode__(self):
        return self.name
