from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, abort
from flask_website.data import database
from flask_website.models import user, product

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return render_template('general/index.html', products=product.Product.query.all())
