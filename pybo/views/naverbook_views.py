from flask import Blueprint,render_template,request,url_for
from werkzeug.utils import redirect
from pybo.naverapi import naverbook
from ..forms import NaverbookForm


bp = Blueprint('naver',__name__,url_prefix='/naver')

#http://127.0.0.1/naver/movie 를 입력하면 화면에 영화정보
#http://127.0.0.1/naver/book 를 입력하면 화면에 책정보


@bp.route('/book/', methods=('GET','POST'))   # 책 검색 접근 페이지.
def Naverbook():
    form = NaverbookForm()   # 검색창 설정 --> forms.py에서 만들기

    if request.method == "POST" and form.validate_on_submit():   # 검색창에 내용을 입력해서 출력할 때.
        result = naverbook(form.search.data)
        # print(result)
        return render_template('naver/naverbook.html', bookinfo_list=result['items'], form=form)

    # result = naverbook('삼국지')  #naverapi.py에 있음
    return render_template('naver/naverbook.html',form=form)  # form html에서 사용하는 변수 오른쪽은 form 데이터

# SQL, NO-SQL

#SQL -> MYSQL, 오라클, 마리아DB, MS-SQL, SQLite

#NO-SQL -> MONGODB, Redis,.........