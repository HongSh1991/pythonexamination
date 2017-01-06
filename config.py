import os
import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))

cf = ConfigParser.ConfigParser()
cf.readfp(open('mydata.ini'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or cf.get("APP", "SECRET_KEY")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
#    MAIL_USERNAME = cf.get("MAIL", "MAIL_USERNAME")
#    MAIL_PASSWORD = cf.get("MAIL", "MAIL_PASSWORD")

    HONGSH_MAIL_SUBJECT_PREFIX = 'HONGSH-DreamSky'
    HONGSH_MAIL_SENDER = '18751970802@163.com'
    HONGSH_ADMIN = 'hjmrezl@outlook.com'
    HONGSH_POSTS_PER_PAGE = 20
    HONGSH_FOLLOWERS_PER_PAGE = 50
    HONGSH_COMMENTS_PER_PAGE = 30

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hs123@127.0.0.1/myflaskproject'
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hs123@localhost/myflaskproject'
# os.environ.get('TEST_DATABASE_URL') or \
#    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'mysql://root:hs123@localhost/myflaskproject'
# % cf.get("MySQL", "MySQL_PASSWORD")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
