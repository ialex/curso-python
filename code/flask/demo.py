
import json
from flask import Flask, request, jsonify
from pymongo import Connection


app = Flask(__name__)
app.debug = True

connection = Connection()
db = connection.game

@app.route("/")
def index():
    player = db.players.find({}, {'_id':0})
    player = [x for x in player]
    data = {'results': player}
    return jsonify(data)

@app.route('/post/', methods=['POST', 'GET'])
def post_data(): 
 
    if request.method == 'POST':
        fields = request.form
    else:
        fields = []
    
    data = {'results': None}
    data['message'] = 'POST RECEIVED'
    data['fields'] = fields
    return jsonify(data)


@app.route('/register/', methods=['POST'])
def register():

    response = {}
    data = {}

    data['name'] = request.form['name']
    data['email'] = request.form['email']
    data['password'] = request.form['password']
    
    db.users.insert(data)
    data.pop('_id')
    
    data['session'] = True
    response['results'] = data
    return jsonify(response)


@app.route('/login/', methods=['POST'])
def login():

    response = {}
    data = {}

    data['email'] = request.form['email']
    data['password'] = request.form['password']
    
    user = db.users.find_one({'email': data['email']})
    if (user['email'] == data['email']) and (user['password'] == data['password']):
        data['session'] = True
    else:
        data['session'] = False

    response['results'] = data
    return jsonify(response)
 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

