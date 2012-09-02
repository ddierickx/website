from flask import Blueprint, render_template 
from flask_website.data import database

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return render_template('general/index.html')
