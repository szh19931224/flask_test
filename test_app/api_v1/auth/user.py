from flask import request
from flask import jsonify
from flask import current_app
from flask import request
from flask_login import current_user, login_user

from test_app.api_v1.auth import auth_bp
from test_app.models import User, Role, Permission, PermissionRoleShip
from test_app import db


@auth_bp.route('/')
def hello_world():
    return 'Hello, World!'


@auth_bp.route('/projects/')
def projects():
    return 'The project page'


@auth_bp.route('/about')
def about():
    return 'The about page'


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.args.get('username', '')
    passwd = request.args.get('passwd', '')
    resp = jsonify({'username': username, 'passwd': passwd})
    return resp

