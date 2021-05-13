from flask import Blueprint,render_template,request,url_for
from pybo.models import Question
from ..forms import QuestionForm, AnswerForm
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect
#127.0.0.1:5000/question/list
#127.0.0.1:5000/question/detail/3

bp = Blueprint('question',__name__,url_prefix='/question')

@bp.route('/list/')
def _list():
    page = request.args.get('page',type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page,per_page=10)
    return render_template('question/question_list.html', question_list=question_list)  # 정해진 웹페이지로 이동해주는 코드.


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form=AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/detail.html',question=question,form=form)

@bp.route('/create/',methods=('GET','POST'))
def create():
    form = QuestionForm()
    if request.method == "POST" and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data,
                            create_date=datetime.now())

        db.session.add(question)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('question/question_form.html',form=form)

# 1. 접속주소생성
# 2. 데이터베이스에서 데이터를 가져온다.
# 3. html로 전달해서 보여준다.