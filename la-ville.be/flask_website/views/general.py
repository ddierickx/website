from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, abort

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    return render_template('general/index.html')
