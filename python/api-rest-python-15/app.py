from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
#from flask_httpauth import HTTPDigestAuth ---1
#from flask_httpauth import HTTPBasicAuth ---1
#from werkzeug.security import generate_password_hash, check_password_hash ---1

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    'token-secreto-1': 'cristian'
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

#app.config['SECRET_KEY'] = 'GDJSJ4773DSHSH' ---2
#auth = HTTPDigestAuth() ---2
#auth = HTTPBasicAuth() ---1

'''users = {
    #'cristian': generate_password_hash('pass1111') ---1
    #'cristian': "pass1111" ---2
} ---1 y ---2'''

#funcion para comprobar si las contrasenas son correctas
'''@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None ---2'''

#funcion para autenticar al usuario
'''@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username ---1'''

@app.route('/user')
@auth.login_required
def get_user():
    return {
        'name': 'Dario',
        'age': 35
    }


if __name__ == '__main__':
    app.run()
