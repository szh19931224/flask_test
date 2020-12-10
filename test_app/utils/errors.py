from flask import jsonify


class BaseError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload

    def __str__(self):
        return self.message

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv


class LoginError(BaseError):
    def __init__(self):
        super(LoginError, self).__init__('login failed')
        self.status_code = 401


class NotLoginError(BaseError):
    def __init__(self):
        super(self.__class__, self).__init__('user not login')
        self.status_code = 401


class MyTestError(BaseError):
    def __init__(self):
        super(MyTestError, self).__init__('this is a test')
        self.status_code = 400


from test_app.api_v1.auth import auth_bp
from test_app.api_v1.test import helloworld_bp


@auth_bp.errorhandler(LoginError)
@auth_bp.errorhandler(NotLoginError)
@helloworld_bp.errorhandler(MyTestError)
def error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response




