from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, PasswordField,EmailField
# from wtforms.validators import DataRequired, Length, EqualTo, Email

from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목',validators=[DataRequired()])
    content = TextAreaField('내용',validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class NaverbookForm(FlaskForm):
    search = StringField('검색창', validators=[DataRequired()])

class MovieInfoForm(FlaskForm):
    search = StringField('검색창', validators=[DataRequired()])

class WeatherInfoForm(FlaskForm):
    search = StringField('검색창', validators=[DataRequired()])

class HelpInfoForm(FlaskForm):
    search = StringField('검색', validators=[DataRequired()])