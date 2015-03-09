from flask import render_template, redirect, url_for
from app import app, db
from models import User, Topic, Question, Answer

@app.route('/')
@app.route('/index')

def index():
    user = { 'nickname': 'Miguel' }
    return render_template ("index.html",
                            title = 'Home',
                            user = user)

@app.route('/questions')
def template():
    # topics = Topic.query.all()
    return render_template ("questions.html")
    # return "Hello"