from werkzeug.middleware.proxy_fix import ProxyFix
from flask_session import Session
from flask import Flask, session
from config import Config
import os

class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


def create_app():
    print("Create App")
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.wsgi_app = ReverseProxied(app.wsgi_app)
    app.secret_key = os.urandom(24)
    print(app.secret_key)

    with app.app_context():
        from . import routes
        return app