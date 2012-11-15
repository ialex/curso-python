
import os
import sys 
import json
import redis
import os.path 
import importlib


if __name__ == '__main__':


    path = os.path.dirname(os.path.abspath(__file__))
    path += '/tasks/' 
    tasks = os.listdir(path)
    tasks = [m for m in tasks if m != '__init__.py' and m.endswith('.py')]

    for task in tasks:
        module = 'tasks.%s' % task.rpartition('.')[0]
        m = importlib.import_module(module)
        print module
        plugin = m.PlugIn()
        response = plugin.response()

    msg = {
        "channels": ["supervisor"],
        "data":{
            'status':response['status'], 
            'user':response['user'], 
            'message':response['message']
            } 
    }

    rc = redis.Redis(host='alvarolizama.net')
    rc.publish("juggernaut", json.dumps(msg))
