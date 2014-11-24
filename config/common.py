import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False

    OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}
    ]

    # Settings for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


try:
    from local import LocalConfig
except ImportError:
    pass