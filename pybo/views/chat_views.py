from flask import Blueprint,render_template,request,url_for
from pybo.models import Question
from pybo.dialogflowapi import chat
from ..forms import QuestionForm, AnswerForm, HelpInfoForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect
#127.0.0.1:5000/question/list
#127.0.0.1:5000/question/detail/3

bp = Blueprint('chat',__name__,url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')

@bp.route('/help/',methods=('GET','POST'))
def Help():
    form = HelpInfoForm()
    if request.method == "POST" and form.validate_on_submit():
        result=chat(form.search.data,'1234')
        print(result)
        if result == '영화 순위 메뉴':
            return redirect(url_for('movie.MovieRank'))
        elif result =='구글':
            return redirect('http://www.google.com')

    return render_template('chat/help.html',form=form)