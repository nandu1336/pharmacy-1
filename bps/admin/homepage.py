from flask import Blueprint,render_template,redirect,flash
from bps.forms import LoginForm

Home = Blueprint('Home', __name__)

@Home.route('/')
def index():
    return redirect('/login')