# -*- coding: utf-8 -*-

"""
    Auth module
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flask import session, redirect


######################################################
###
### Auth 
###
######################################################


class Auth(object):
    """
        Auth and Login system 
    """

    login_url = '/users/login/'
    logout_url = '/users/logout/'
    next_login_url = '/dashboard/'
    next_logout_url = '/'
    disabled_user_url = '/users/disabled/'

    def login(self, id, active=True):
        """
            Login user
        """
        session['user'] = {
                'id': id,
                'active': active
                }
        self.next_login_url
        return redirect(self.next_login_url)

    def logout(self):
        """
            Logout user
        """
        session.pop('user', None)
        return redirect(self.next_logout_url)

    def require_login(self, f):
        """
            Decorator
            Check is an user is logged
        """
        def decorator(*args, **kwargs):
            if session.get('user') is not None:
                user = session.get('user')
                if user['active']:
                    return f(*args, **kwargs)
                else:
                    return redirect(self.disabled_user_url)
            else:
                return redirect(self.login_url)
        return decorator

    @property
    def get_user_id(self):
        """
            Return user id
        """
        return session['user']['id']
