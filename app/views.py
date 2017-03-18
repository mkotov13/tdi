from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Max'} # mock user
    questions = [
        {
            'author': { 'name': 'Michael L.'},
            'body': 'What"s the circumference of Earth on the equator?'
        },
        {
            'author': { 'name': 'Christian M.'},
            'body': 'How many years have the Data Incubator been around for?'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            questions=questions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                            title='Sign In',
                            form=form)

@app.route('/testing')
def testing():
    return "Are we here?"
