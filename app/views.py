from flask import Flask, render_template, flash, redirect, url_for, request
from app import app, db
# from forms import LoginForm
from models import User, Topic, Question, Answer

@app.route('/')
@app.route('/index')

def index():
    user = { 'nickname': 'Miguel' }
    return render_template ("index.html",
                            title = 'Home')

# @app.route('/login', method = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template ('login.html',
#                             form = form)

@app.route('/programming')
def programming():
    topics = Topic.query.all()
    return render_template ("programming.html",
                            topics = topics)
    # return "Hello"

@app.route('/ask_question')
def ask_question():
    if 'question_body' in request.values:
        topics = Topic.query.all()
        print('1111111')
        print(request.values ['question_body'])
        new_topic = Topic()
        new_topic.topic_name = request.values ['question_body']
        db.session.add(new_topic)
        db.session.commit()
        return redirect(url_for('ask_question'))
    else:
        print('222222')
        topics = Topic.query.all()
        return render_template ("ask_question.html",
                                topics = topics)
    # return "Hello"

def add_new_dict_device_type (request):
    new_dict_device_type = device_type()
    new_dict_device_type.type = request.GET['add_dict_device_type.type']
    new_dict_device_type.save()
    return (redirect('/dict_device_type'))