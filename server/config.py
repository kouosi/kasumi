class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.sqlite3'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///production.sqlite3'
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': Config,
}
