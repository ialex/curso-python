# -*- coding: utf-8 -*-

"""
    Base Flask App
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import os.path
from flask import Flask 


######################################################
###
### Setup Main App
###
######################################################

app = Flask(__name__)

if os.path.isfile('settings/development.cfg'):
    app.config.from_pyfile('settings/development.cfg', silent=True)
    print " * Load development settings"
else:
    app.config.from_pyfile('settings/production.cfg', silent=True)
    print " * Load production settings"


######################################################
###
### Mount apps
###
######################################################

from apps.main import app as main_app
from apps.users import app as users_app

app.register_blueprint(main_app)
app.register_blueprint(users_app, url_prefix='/users')

