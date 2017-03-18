from flask import render_template
from app import app

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

@app.route('/testing')
def testing():
    return "Are we here?"
