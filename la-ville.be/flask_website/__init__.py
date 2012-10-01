from flask import Flask, session, g, render_template
from flask_website.data import database
from flask_website.models import user, product, productimage, color, productgroup
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView

def init_cfg(app):
	# Load from file first.
	app.config.from_object('flask_website.configuration')
	# Then try loading from ENV_VAR.
	try:
		app.config.from_envvar('FLASK_WEBSITE_CFG')
	except:
		pass

def init_logging(app):
	import logging
	from logging.handlers import TimedRotatingFileHandler
	formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
	                              "%Y-%m-%d %H:%M:%S")
	file_handler = TimedRotatingFileHandler("logs/app.log")
	file_handler.setFormatter(formatter)
	file_handler.setLevel(logging.WARNING)
	app.logger.addHandler(file_handler)

def init_admin(app, db):
	admin = Admin(app, name="La Ville")
	admin.add_view(ModelView(product.Product, db.session))
	admin.add_view(ModelView(color.Color, db.session))
	admin.add_view(ModelView(productgroup.ProductGroup, db.session))


def init_flask():
	# Initialize app!
	app = Flask(__name__)
	# Needed for Flask-admin.
	app.secret_key = "secret"
	init_logging(app)
	init_cfg(app)

	# Add 404 error handler.
	@app.errorhandler(404)
	def not_found(error):
	    return render_template('404.html'), 404

	# Initialize blueprints.
	from flask_website.views import general, store, store_api
	app.register_blueprint(general.mod)
	app.register_blueprint(store.mod)
	app.register_blueprint(store_api.mod)

	db = database.Database()
	db.init_db(app)

	init_admin(app, db)
	#init_test_db(db)

	# Utility functions for Jinja2.
	app.jinja_env.globals.update(jsonBoolean=lambda b: str(b).lower())
	
	return app

def init_test_db(db):
	# Small DB test => REMOVE
	prod1 = product.Product(name="Hanger model",
				short_description="Short description",
				image_url="content/product_images/hanger model.jpg",
				price=39.99,
				stock=10,
				color="red",
				discontinued=False)
	img1 = productimage.ProductImage("an_url")

	prod1.product_images.append(img1)

	db.session.add_all([prod1, img1])
	db.session.commit()
