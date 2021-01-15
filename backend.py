from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        subdict = {'users_list': []}
        if search_username and search_job:
            findict = {'users_list': []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    findict['users_list'].append(user)
            for user in findict['users_list']:
                if user['job'] == search_job:
                    subdict['users_list'].append(user)
        elif search_username:
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
        elif search_job:
            for user in users['users_list']:
                if user['job'] == search_job:
                    subdict['users_list'].append(user)
        else:
            return users
        if subdict == {'users_list': []}:
            resp = jsonify({"Msg": "User not found within provided search."})
            return resp
        else:
            return subdict
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = uuid.uuid4()
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd),201
        return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                if request.method == 'GET':
                    return user
                elif request.method == 'DELETE':
                    users['users_list'].remove(user)
                    resp = jsonify(), 204
                    return resp
        resp = jsonify({"Msg": "User not found with provided id."}), 404
        return resp
    return users


users = {
    'users_list':
        [
            {
                'id': 'xyz789',
                'name': 'Charlie',
                'job': 'Janitor',
            },
            {
                'id': 'abc123',
                'name': 'Mac',
                'job': 'Bouncer',
            },
            {
                'id': 'ppp222',
                'name': 'Mac',
                'job': 'Professor',
            },
            {
                'id': 'yat999',
                'name': 'Dee',
                'job': 'Aspring actress',
            },
            {
                'id': 'zap555',
                'name': 'Dennis',
                'job': 'Bartender',
            }
        ]
}
