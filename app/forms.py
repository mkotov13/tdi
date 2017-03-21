from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class QuestionForm(Form):
    body = TextAreaField('body', validators=[DataRequired()])
    right_answer = StringField('right_answer', validators=[DataRequired()])
    feedback = TextAreaField('feedback', validators=[DataRequired()])

class AnswerForm(Form):
    answer = StringField('answer', validators=[DataRequired()])
