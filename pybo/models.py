from pybo import db

class Question(db.Model):    # Question은 테이블 이름
    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(200),nullable=False)
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id',ondelete='CASCADE'))
    question = db.relationship('Question',backref=db.backref('answer_set'))
    content = db.Column(db.Text(),nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)

# 회원 정보
class Userinfo(db.Model):
    user_id = db.Column(db.Text(), primary_key=True)
    #user_pw= db.Column(db.Integer, db.ForeignKey('user_name',ondelete='CASCADE'))
    #user_name = db.relationship('Question',backref=db.backref('answer_set'))
    user_pw = db.Column(db.Integer(), nullable=False)
    user_name = db.Column(db.Text(), nullable=False)
    user_age = db.Column(db.Integer(),nullable=False)
    user_add = db.Column(db.Text(), nullable=False)
    user_sex = db.Column(db.Text(), nullable=False)
    user_sch = db.Column(db.Text(), nullable=False)
    user_hby = db.Column(db.Text(), nullable=False)
    user_date = db.Column(db.Integer(), nullable=False)
    create_date = db.Column(db.DateTime(),nullable=False)

# 아이디, 패스워드 등록
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)

# 미스터트롯 투표 등록
class Vote(db.Model):
    mrname = db.Column(db.String(150),primary_key=True)
    votecount = db.Column(db.Integer,nullable=False)



