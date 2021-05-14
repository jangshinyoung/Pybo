# 코딩 순서 바뀌면 안됨.

from flask import Flask

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)


# SQLAlchemy 설정
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)

from. import models

from .views import main_views,question_views,answer_views,auth_views,naverbook_views,movie_views
app.register_blueprint(main_views.bp)
app.register_blueprint(question_views.bp)
app.register_blueprint(answer_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(naverbook_views.bp)
app.register_blueprint(movie_views.bp)

from .filter import format_datetime
app.jinja_env.filters['datetime'] = format_datetime


