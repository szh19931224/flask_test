from flask import jsonify
from flask import request

from test_app.api_v1.test import helloworld_bp
from test_app.utils.errors import MyTestError
from test_app.models import Test
from test_app import db


@helloworld_bp.route('/', methods=['GET'])
@helloworld_bp.route('/say_hello', methods=['GET'])
def hello_world():
    msg = 'hello world'
    status_code = 200
    data = {}
    return jsonify({'msg': msg, 'status_code': status_code, 'data': data})


@helloworld_bp.route('/add_string', methods=['POST'])
def add_string():
    if not request.args.get('test_string'):
        raise MyTestError()
    test = Test(test_string=request.args.get('test_string'))
    db.session.add(test)
    db.session.commit()

    msg = 'ok'
    status_code = 200
    data = {}
    return jsonify({'msg': msg, 'status_code': status_code, 'data': data})
