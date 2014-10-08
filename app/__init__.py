from flask import Flask
from flask.ext.bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap()
bootstrap.init_app(app)

from app import views

basedir =  os.path.abspath(os.path.dirname(__file__))
config_py = os.path.join(basedir, '../config.py')
if not os.path.isfile(config_py):
    import shutil
    config = os.path.join(basedir, '../config')
    shutil.copyfile(config, config_py)