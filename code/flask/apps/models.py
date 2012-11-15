# -*- coding: utf-8 -*-

"""
    Models for mongo
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from modules.mongo import Mongo


######################################################
###
### Models
###
######################################################

class User(Mongo):

    def get_active_users(self):
        return self.collection.find({'active': True})
