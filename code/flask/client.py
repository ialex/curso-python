
import requests 


session = False
url = 'http://127.0.0.1:5000/'


def check_login(f):
    def wrap():
        if session:
            return f()
        else:
            print  "No login"
    return wrap


def register():

    global session

    params = {'name': 'Alvaro',
            'email': 'nekrox@gmail.com',
            'password': 'dfsdfdsf'
            }

    u = url + 'register/'
    r = requests.post(u, data=params)
    
    json_data = r.json
    session = json_data['results']['session']
    return session


def login():

    global session

    params = {
            'email': 'nekrox@gmail.com',
            'password': 'dfsdfdsf'
            }

    u = url + 'login/'
    r = requests.post(u, data=params)
    
    json_data = r.json
    session = json_data['results']['session']
    return session


@check_login
def status():
    print "status"


def switch(opt):

    cases = {
            'register': register,
            'login': login,
            'check_login': check_login,
            'status': status
            }

    return cases[opt]


if __name__ == '__main__':

    print "######################"
    print "Opciones:"
    print "register"
    print "login"
    print "status"
    print "######################"
    while True:
        print session
        opt = raw_input('>> ') 
        switch(opt)()

