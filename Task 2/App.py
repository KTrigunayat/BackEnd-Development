
from flask import Flask, request, redirect, session, url_for, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management



CLIENT_ID = "Ov23lic6grHh4EtItFO5"
CLIENT_SECRET = "1639a4d53d53185fa1685814e167b8001bb1eddc"
AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
API_BASE_URL = "https://api.github.com/user"


USERNAME = "Kshitiz"
PASSWORD = "AU23UG008"

@app.route('/basic-auth', methods=['GET'])
def basic_auth():
    authorization = request.authorization
    if not authorization or not authorization.username or not authorization.password:
        return jsonify({"message": "Unauthorized"}), 401
    if authorization.username == USERNAME and authorization.password == PASSWORD:
        return jsonify({"message": "Authorized"}), 200
    return jsonify({"message": "Unauthorized"}), 401


@app.route('/bearer-auth', methods=['GET'])
def bearer_auth():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Unauthorized"}), 401
    if auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        if token == "AU23UG008":
            return jsonify({"message": "Authorized"}), 200
    return jsonify({"message": "Unauthorized"}), 401



@app.route('/home', methods=['GET'])
def home():
    return '''
        <h1>Home Page</h1>
        <a href="/login">Login with GitHub</a>
    '''

@app.route('/login')
def login():
    # Redirect to GitHub for authorization
    return redirect(f"{AUTHORIZATION_BASE_URL}?client_id={CLIENT_ID}&scope=user")

@app.route('/callback')
def oauth_callback():
    code = request.args.get('code')
    if not code:
        return jsonify({"message": "Missing code parameter"}), 400
    
    # Exchange code for access token
    response = requests.post(TOKEN_URL, data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
    }, headers={'Accept': 'application/json'})
    
    token_info = response.json()
    access_token = token_info.get('access_token')
    
    if access_token:
        # Fetch user information
        user_response = requests.get(API_BASE_URL, headers={
            'Authorization': f'token {access_token}'
        })
        user_info = user_response.json()
        return jsonify(user_info), 200

    return jsonify({"message": "Failed to obtain access token"}), 400

if __name__ == '__main__':
    app.run(debug=True)