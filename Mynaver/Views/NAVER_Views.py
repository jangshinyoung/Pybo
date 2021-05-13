from flask import Blueprint
NVdv = Blueprint('NAVER',__name__,url_prefix='/naver')

@NVdv.route('/movie')
def NAVER_movie():
    return '영화정보입니다.'
