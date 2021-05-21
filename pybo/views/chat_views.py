from flask import Blueprint,render_template,request,url_for
from pybo.models import Question
from ..forms import QuestionForm, AnswerForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect
#127.0.0.1:5000/question/list
#127.0.0.1:5000/question/detail/3

bp = Blueprint('chat',__name__,url_prefix='/chat')

@bp.route('/bot/')
def Bot():
    return render_template('chat/chatbot.html')