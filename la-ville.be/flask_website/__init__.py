from flask import Flask, session, g, render_template
from flask_website.database import db
from flask_website.models import user
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)
#app.config.from_object('websiteconfig')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from flask_website.views import general
app.register_blueprint(general.mod)

import logging
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
file_handler = TimedRotatingFileHandler("logs/app.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

app.logger.debug("lala")
app.logger.warning("lolo")
app.logger.error("lili")

#ed_user = user.User('Ed Jones', 'edsemail')
#session = db.db_session
#session.add(ed_user)
#session.commit()
#print ed_user
