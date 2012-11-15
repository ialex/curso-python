# -*- coding: utf-8 -*-

"""
    Main Flask App
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flask import Blueprint, render_template
from modules.auth import Auth

app = Blueprint('main', __name__,
                        template_folder='templates',
                        static_folder='statics')


######################################################
###
### Routes
###
######################################################

@app.route('/')
def index():
    return render_template('main/index.html')
