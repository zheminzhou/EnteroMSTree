from flask import Flask
import config
import sys
import os

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'grapetree','templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))), static_folder=static_folder)
else:
    app = Flask(__name__) # , static_folder='static/', template_folder='templates/')

app.config.from_object(config)

from grapetree import views
