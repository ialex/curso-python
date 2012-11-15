# -*- coding: utf-8 -*-

"""
    User App
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

import bcrypt
from flask import Blueprint
from flask import session, redirect, render_template, flash
from modules.auth import Auth
from apps.models import User
from apps.forms import RegisterUserForm, LoginUserForm


app = Blueprint('users', __name__,
                        template_folder='templates',
                        static_folder='statics')


######################################################
###
### SetUps
###
######################################################

auth = Auth()

######################################################
###
### Routes
###
######################################################

@app.route('/register/', methods=['GET', 'POST'])
def user_register():
    """
        Register an user
    """
    if 'user' in session:
        return redirect('/dashboard/')

    form = RegisterUserForm(csrf_enabled=False)

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        user = User()
        result = user.find_one({'email': email})

        if result is None:
            data = {
                    'name': name,
                    'email': email,
                    'password': bcrypt.hashpw(password, bcrypt.gensalt()),
                    'is_active':True
                    }
            id = user.insert(data)
            return auth.login(id=id, active=data['is_active'])
        else:
            flash('El correo esta registrado, prueba con otro', 'error')
    return render_template('users/register.html', form=form) 
     

@app.route('/login/', methods=['GET', 'POST'])
def user_login():
    """
        Login an user
    """
    if 'user' in session:
        return redirect('/dashboard')

    form = LoginUserForm(csrf_enabled=False)

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        user = User()
        result = user.find_one({'email': email})
       
        if result is not None:
            if bcrypt.hashpw(password, result['password']) == result['password']:
                return auth.login(id=result['_id'], active=result['is_active'])
            else:
                flash('Password incorrecto', 'error')
        else:
            flash('El usuario no existe', 'error')
    return render_template('users/login.html', form=form) 


@app.route('/logout/', methods=['GET'])
def user_logout():
    """
        Logout an user
    """
    if 'user' in session:
        return auth.logout()
    else:
        return redirect('/')
