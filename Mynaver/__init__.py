from flask import Flask

def create_app():
    app = Flask(__name__)

    from .Views import NAVER_Views
    app.register_blueprint(NAVER_Views.NVdv)

    return app