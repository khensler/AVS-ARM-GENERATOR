import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    secret_key = os.environ.get('SECRET_KEY') or 'you-will-never-guess'