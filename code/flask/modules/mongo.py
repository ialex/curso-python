# -*- coding: utf-8 -*-

"""
    Mongo Adapter
    Author  :   Alvaro Lizama Molina <nekrox@gmail.com>
"""

from flask import current_app
from pymongo import Connection


######################################################
###
### Mongo connection and base model
###
######################################################

class Mongo(object):
    """ Mongo Model """

    db = None
    collection = None

    def __init__(self):
        """ Connect with mongo """
        connection = Connection()
        self.db = connection[current_app.config['MONGO_DB_NAME']]
        self.collection = self.db[self.__class__.__name__.lower()]

    def get_db(self):
        return self.db

    def get_collection(self, collection):
        return self.db[collection] 

    def get_collections(self):
        return self.db.collection_names()
    
    def insert(self, data):
        return self.collection.insert(data, safe=True)

    def find_one(self, query=None):
        return self.collection.find_one(query)

    def find(self, query=None, fields=None, skip=0, limit=0):
        return self.collection.find(query, fields, skip=skip, limit=limit)

    def update(self, query, data, upsert=True, multi=True):
        return self.collection.update(query, data, upsert=upsert, 
                multi=multi, safe=True)
    
    def remove(self, data):
        return self.collection.remove(data, safe=True)

    def count(self):
        return sel.collection.count()
