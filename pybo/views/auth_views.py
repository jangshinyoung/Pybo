from flask import Blueprint, render_template, request, url_for, flash, session, g
from pybo.models import User
from werkzeug.security import generate_password_hash, check_password_hash

from pybo.models import Question
from ..forms import QuestionForm, AnswerForm, UserCreateForm, UserLoginForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect

bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/signup',methods=('GET','POST'))
def signup():
    form = UserCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user=User(username=form.username.data,
                      password=generate_password_hash(form.password1.data),
                      email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자 입니다.')


    return render_template('auth/signup.html',form=form)




@bp.route('/login/',methods=('GET','POST'))
def login():
    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = '존재하지 않는 사용자입니다.'
        elif not check_password_hash(user.password,form.password.data):
            error = '비밀번호를 잘못 입력되었습니다.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))

        flash(error)

    return render_template('auth/login.html',form=form)


@bp.before_app_request    # 유저의 저장 정보.
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else :
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))