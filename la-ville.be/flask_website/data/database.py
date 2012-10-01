from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
   def __init__(self):
   	pass

   def init_db(self, app):
	self.engine = create_engine(app.config["DATABASE"], convert_unicode=True, echo=True)
	self.session = scoped_session(sessionmaker(autocommit=False,
	                                         autoflush=False,
	                                         bind=self.engine))
	Base.query = self.session.query_property()
	app.logger.debug("Initializing database.")
	from flask_website.models import user
	from flask_website.models import product
	from flask_website.models import productimage
	from flask_website.models import color
	from flask_website.models import productgroup
	Base.metadata.create_all(bind=self.engine)
	app.logger.debug("Database initialized.")
