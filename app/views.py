from flask import Flask, session, render_template, flash, redirect, url_for, request, abort, g
from app import app, db, login_manager
from flask.ext.login import login_user, logout_user, current_user, login_required
# from forms import LoginForm
from models import User, Topic, Question, Answer


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
    reg_user = User()
    reg_user.username = request.form['username']
    reg_user.password = request.form['password']
    reg_user.email = request.form['email']
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
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index')
def index():
    # user = { 'nickname': 'Miguel' }
    return render_template ("index.html")

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
        # print('1111111')
        # print(request.values ['question_body'])
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