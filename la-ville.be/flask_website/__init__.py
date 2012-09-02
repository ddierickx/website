from flask import Flask, session, g, render_template
from flask_website.data import database
from flask_website.models import user, product

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


def init_flask():
	# Initialize app!
	app = Flask(__name__)
	init_logging(app)
	init_cfg(app)

	# Add 404 error handler.
	@app.errorhandler(404)
	def not_found(error):
	    return render_template('404.html'), 404

	# Initialize blueprints.
	from flask_website.views import general
	app.register_blueprint(general.mod)


	# Small DB test => REMOVE
	db = database.Database()
	db.init_db(app)

	prod1 = product.Product("Hanger model", "content/product_images/hanger model.jpg", 39.99)
	prod2 = product.Product("Hanger model", "content/product_images/kraagje collar dondergroen.jpg", 49.99)
	prod3 = product.Product("Hanger model", "content/product_images/kraag collar 1deel oranje.jpg", 39.99)
	prod4 =	product.Product("Hanger model", "content/product_images/kraag collar 1deel bordeaux.jpg", 29.99)

	#db.session.add(prod1)
	#db.session.add_all([prod1, prod2, prod3, prod4])
	#db.session.commit()

	return app
