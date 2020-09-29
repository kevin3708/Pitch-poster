import os

class Config:
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://kevin:Password2@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = "kevin"


    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/pitches'
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production': ProdConfig,
}