# -*- coding: utf-8 -*-

import os
import flask
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery

CLIENT_SECRETS_FILE = "file.json"

SCOPES = ['openid https://www.googleapis.com/auth/drive.metadata.readonly https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email']
API_SERVICE_NAME = 'drive'
API_VERSION = 'v2'

app = flask.Flask(__name__)
app.secret_key = 'fh6k56nsdFGHF%/%45njsdk3469'

#permite lanzar proceso autenticacion
@app.route('/')
def index():
  return print_index_table()


@app.route('/user')
def test_api_request():
  if 'credentials' not in flask.session:
    return flask.redirect('authorize')

  credentials = google.oauth2.credentials.Credentials(
      **flask.session['credentials'])

  drive = googleapiclient.discovery.build(
      API_SERVICE_NAME, API_VERSION, credentials=credentials)

  flask.session['credentials'] = credentials_to_dict(credentials)

  return {
      'user': 'Dario',
      'age': 16
  }


@app.route('/authorize')
def authorize():
  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES)

  flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  authorization_url, state = flow.authorization_url(
      access_type='offline',
      include_granted_scopes='true')
  flask.session['state'] = state

  return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
  state = flask.session['state']

  flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
      CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
  flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

  authorization_response = flask.request.url
  flow.fetch_token(authorization_response=authorization_response)
  credentials = flow.credentials
  flask.session['credentials'] = credentials_to_dict(credentials)

  return flask.redirect(flask.url_for('test_api_request'))


def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

def print_index_table():
  return ('<table>' +
          '<tr><td><a href="/user">Obtener usuario</a></td>' +
          '</tr>' +
          '</table>')


if __name__ == '__main__':
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE']= '1'

  app.run('localhost', 8082, debug=True)