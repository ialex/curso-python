# -*- coding: utf-8 -*-

"""
    Forms
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flask.ext.wtf import Form, TextField, FloatField, PasswordField
from flask.ext.wtf import SelectField, Required, TextAreaField, Email


######################################################
###
### Forms 
###
######################################################

class RegisterUserForm(Form):
    name = TextField(u'Nombre', validators=[Required()])
    email = TextField(u'Email', validators=[Required(), Email()])
    password = PasswordField(u'Password', validators=[Required()])

class LoginUserForm(Form):
    email = TextField(u'Email', validators=[Required()])
    password = PasswordField(u'Password', validators=[Required()])

