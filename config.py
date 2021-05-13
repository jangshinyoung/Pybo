import os

BASE_DIR = os.path.dirname(__file__)   # 현재 폴더경로 가져오는 명령

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))  #소괄호안의 글자는 중괄호에 들어간다.
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY='dev'