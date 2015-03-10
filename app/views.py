from flask import Flask, session, render_template, flash, redirect, url_for, request, abort, g
from app import app, db, login_manager
from flask.ext.login import login_user, logout_user, current_user, login_required
# from forms import LoginForm
from models import User, Topic, Question, Answer
from datetime import datetime

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.form['username'] == User.query.filter_by(username=request.form['username']):
        flash('Username has already exist', 'error')
        return redirect(url_for('login'))
    reg_user = User()
    reg_user.username = request.form['username']
    reg_user.password = request.form['password']
    reg_user.email = request.form['email']
    reg_user.registered_on = datetime.utcnow()
    db.session.add(reg_user)
    db.session.commit()
    flash ('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember = remember_me)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
# @login_required
def index():
    # user = { 'nickname': 'Miguel' }
    return render_template ("index.html")


@app.route('/programming')
# @login_required
def programming():
    topics = Topic.query.all()
    return render_template ("programming.html",
                            topics = topics)
    # return "Hello"

@app.route('/ask_question', methods=['GET','POST'])
@login_required
def ask_question():
    if request.method == 'GET':
        topics = Topic.query.all()
        return render_template('ask_question.html',
                               topics = topics)

@app.route('/add_question', methods=['GET','POST'])
@login_required
def add_question():
    if 'question_body' in request.values:
        topics = Topic.query.all()
        topic_id = request.form['question_topic']
        my_topic = Topic.query.get(topic_id)
        new_question = Question()
        new_question.question_body = request.form['question_body']
        new_question.topic_id = my_topic.id
        new_question.timestamp = datetime.utcnow()
        new_question.user_id = g.user.id
        db.session.add(new_question)
        db.session.commit()
        flash ('Question successfully added')
        return redirect(url_for('index'))


def add_new_dict_device_type (request):
    new_dict_device_type = device_type()
    new_dict_device_type.type = request.GET['add_dict_device_type.type']
    new_dict_device_type.save()
    return (redirect('/dict_device_type'))