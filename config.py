class Config:
    SECRET_KEY = 'ha le ge ha'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    ENV = 'production'
    # SERVER_NAME = '127.0.0.1:8123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@localhost/flask_test'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    # SERVER_NAME = '127.0.0.1:8123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123123@localhost/flask_test'


config = {
    'default': DevelopmentConfig,
    'production': ProductionConfig
}
