from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from app import app, db, lm, oid
from .forms import LoginForm, QuestionForm, AnswerForm
from .models import User, Question, Answer


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    user = g.user
    form = QuestionForm()
    if form.validate_on_submit():
        question = Question(body=form.body.data, right_answer=form.right_answer.data, feedback=form.feedback.data, author=user)
        db.session.add(question)
        db.session.commit()
        flash('Your question has been added')
        return redirect(url_for('index'))
    questions = Question.query.all()
    # mock questions
    quesns = [
        {
            'author': { 'nickname': 'Michael L.'},
            'body': 'What"s the circumference of Earth on the equator?'
        },
        {
            'author': { 'nickname': 'Christian M.'},
            'body': 'How many years have the Data Incubator been around for?'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            form=form,
                            questions=questions)

@app.route('/question/<id>', methods=['GET', 'POST'])
@login_required
def question(id):
    user = g.user
    question = Question.query.filter_by(id=id).first()
    if question == None:
        flash('Question #%s not found.' % id)
        return redirect(url_for('index'))
    form = AnswerForm()
    if form.validate_on_submit():
        answer = Answer(answeredby=user, question=question, answer=form.answer.data, timestamp=datetime.utcnow())
        db.session.add(answer)
        db.session.commit()
        flash('Your answer has been submitted')
        return render_template('feedback.html',
                               title='checking',
                               q=question,
                               a=answer,
                               user=user)
    return render_template('question.html',
                           title='Submit an Answer',
                           q=question,
                           form=form,
                           user=user)

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# testing routes
@app.route('/testing')
def testing():
    return "Are we here?"

# error handlers
@app.errorhandler(401)
def not_authorized_error(error):
    return render_template('401.html'), 401
