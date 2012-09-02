from flask import Blueprint, render_template
from flask_website.models import product
from flask_website.utils import json

mod = Blueprint('store_api', __name__)

@mod.route('/store/api/1/products')
@json.wrap_json_response
def products():
    return products_to_json(product.Product.query.all())

@json.wrap_meta_list
def products_to_json(products):
	return "[" + ",".join(map(lambda p: render_template("store_api/product.json", product = p), products)) + "]"
