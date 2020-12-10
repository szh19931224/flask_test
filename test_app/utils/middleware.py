from flask import request
from flask_login import login_user

from test_app.api_v1.auth import auth_bp
from test_app.models import User
from errors import LoginError, NotLoginError


@auth_bp.before_request
def auth():
    if not (request.args.get('username') and request.args.get('token')):
        raise NotLoginError
    else:
        user = User.query.filter_by(username=request.args.get('username')).\
            filter_by(token=request.args.get('token')).first()
    if user:
        login_user(user)
    else:
        raise LoginError
