#!/usr/bin/env python3
"""
API entry point
"""
from os import getenv
from flask import Flask, jsonify, request, abort
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv("AUTH_TYPE")

if auth_type == "basic_auth":
    auth = BasicAuth()
elif auth_type == "session_auth":
    auth = SessionAuth()

@app.before_request
def before_request():
    """
    Before request handler
    """
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/',
                      '/api/v1/auth_session/logout/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None and auth.session_cookie(request) is None:
        abort(401)
    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)

@app.errorhandler(404)
def not_found(error):
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(401)
def unauthorized(error):
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden(error):
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403

@app.teardown_appcontext
def teardown_db(exception):
    """ Closes storage session """
    storage.close()

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
