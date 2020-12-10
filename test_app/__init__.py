# -*- encoding: utf-8 -*-
import logging
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

# 如果有可能的话，应当在创建应用对象之前配置日志; so here
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.getcwd() + '/test.log',
                    filemode='a+')

db = SQLAlchemy(session_options={'autocommit': False})


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login_views'

    from test_app.utils import middleware

    from api_v1.auth import auth_bp as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth')

    from api_v1.test import helloworld_bp as helloworld_blueprint
    app.register_blueprint(helloworld_blueprint, url_prefix='/api/v1/test')

    return app


