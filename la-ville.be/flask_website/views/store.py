from flask import Blueprint, render_template
from flask_website.models import product

mod = Blueprint('store', __name__)

@mod.route('/products.html')
def index():
    return render_template('store/products.html', products=product.Product.query.all())
