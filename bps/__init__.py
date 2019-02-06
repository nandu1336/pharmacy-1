from flask import Flask,Blueprint
from bps.admin.homepage import Home
from bps.admin.account import Login,Register
from bps.main.working import Dashboard
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(Home, url_prefix='/')
app.register_blueprint(Login, url_prefix='/')
app.register_blueprint(Register, url_prefix='/')
app.register_blueprint(Dashboard, url_prefix='/')