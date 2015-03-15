from flask import Flask, session, render_template, flash, redirect, url_for, request, abort, g
from app import app, db, login_manager
from flask.ext.login import login_user, logout_user, current_user, login_required
# from forms import LoginForm
from models import Users, Topic, Question, Answer
from datetime import datetime

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.form['username'] == Users.query.filter_by(username=request.form['username']):
        flash('Username has already exist', 'error')
        return redirect(url_for('login'))
    reg_user = Users()
    reg_user.username = request.form['username']
    reg_user.password = request.form['password']
    reg_user.email = request.form['email']
    reg_user.registered_on = datetime.utcnow()
    db.session.add(reg_user)
    db.session.commit()
    flash ('User successfully registered')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = Users.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))
    login_user(registered_user, remember=remember_me)
    flash('Logged in successfully')
    return redirect(url_for('index'))


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


@app.route('/contact')
def contact():
    return render_template ("contact.html")


@app.route('/about')
def about():
    return render_template ("about.html")

#################################
## Templates for question list ##
#################################

@app.route('/programming', methods=['GET','POST'])
def programming():
    if 'topic_name' in request.values:
        if request.form['topic_name'] == 'Programming':
            current_topic = request.form['topic_name']
            current_topic_id = Topic.query.filter_by(topic_name=current_topic).first()
            current_topic_id=current_topic_id.id
            topics = Topic.query.all()
            questions = Question.query.filter_by(topic_id=current_topic_id)
            users = Users.query.all()
            return render_template("template.html",
                                   current_topic = current_topic,
                                   questions=questions,
                                   users=users,
                                   topics = topics)
    else:
        return "Something going wrong"

@app.route('/hardware', methods=['GET','POST'])
def hardware():
    if 'topic_name' in request.values:
        if request.form['topic_name'] == 'Hardware':
            current_topic = request.form['topic_name']
            current_topic_id = Topic.query.filter_by(topic_name=current_topic).first()
            current_topic_id=current_topic_id.id
            topics = Topic.query.all()
            # return (current_topic)
            questions = Question.query.filter_by(topic_id=current_topic_id)
            users = Users.query.all()
            return render_template("template.html",
                                   current_topic = current_topic,
                                   questions=questions,
                                   users=users,
                                   topics = topics)
    else:
        return "Something going wrong"

@app.route('/software', methods=['GET','POST'])
def software():
    if 'topic_name' in request.values:
        if request.form['topic_name'] == 'Software':
            current_topic = request.form['topic_name']
            current_topic_id = Topic.query.filter_by(topic_name=current_topic).first()
            current_topic_id=current_topic_id.id
            topics = Topic.query.all()
            questions = Question.query.filter_by(topic_id=current_topic_id)
            users = Users.query.all()
            return render_template("template.html",
                                   current_topic = current_topic,
                                   questions=questions,
                                   users=users,
                                   topics = topics)
    else:
        return "Something going wrong"

@app.route('/networking', methods=['GET','POST'])
def networking():
    if 'topic_name' in request.values:
        if request.form['topic_name'] == 'Networking':
            current_topic = request.form['topic_name']
            current_topic_id = Topic.query.filter_by(topic_name=current_topic).first()
            current_topic_id=current_topic_id.id
            topics = Topic.query.all()
            questions = Question.query.filter_by(topic_id=current_topic_id)
            users = Users.query.all()
            return render_template("template.html",
                                   current_topic = current_topic,
                                   questions=questions,
                                   users=users,
                                   topics = topics)
    else:
        return "Something going wrong"

@app.route('/telephony', methods=['GET','POST'])
def telephony():
    if 'topic_name' in request.values:
        if request.form['topic_name'] == 'Telephony':
            current_topic = request.form['topic_name']
            current_topic_id = Topic.query.filter_by(topic_name=current_topic).first()
            current_topic_id=current_topic_id.id
            topics = Topic.query.all()
            questions = Question.query.filter_by(topic_id=current_topic_id)
            users = Users.query.all()
            return render_template("template.html",
                                   current_topic = current_topic,
                                   questions=questions,
                                   users=users,
                                   topics = topics)
    else:
        return "Something going wrong"

@app.route('/other', methods=['GET','POST'])
def other():
    if 'topic_name' in request.values:
        if request.form['topic_name'] == 'Other':
            current_topic = request.form['topic_name']
            current_topic_id = Topic.query.filter_by(topic_name=current_topic).first()
            current_topic_id=current_topic_id.id
            topics = Topic.query.all()
            questions = Question.query.filter_by(topic_id=current_topic_id)
            users = Users.query.all()
            return render_template("template.html",
                                   current_topic = current_topic,
                                   questions=questions,
                                   users=users,
                                   topics = topics)
    else:
        return "Something going wrong"
##############################
## Question Templates ended ##
##############################


@app.route('/ask_question', methods=['GET','POST'])
@login_required
def ask_question():
    if request.method == 'GET':
        topics = Topic.query.all()
        return render_template('ask_question.html',
                               topics=topics)

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

        # if my_topic.topic_name == 'Programming':
        #     return redirect(url_for('/programming'))
        # elif my_topic.topic_name == 'Hardware':
        #     return redirect(url_for('/hardware'))
        # else:
        return redirect(url_for('index'))

##########################
## Template for answers ##
##########################

@app.route('/answers')
def answers():
    question_id=request.values['question_id']
    answers = Answer.query.filter_by(question_id=question_id)
    current_question=Question.query.get(int(question_id))
    users = Users.query.all()
    current_user = Users.query.get(int(current_question.user_id))
    return render_template('template_answers.html',
                           answers=answers,
                           current_question=current_question,
                           current_user=current_user,
                           users=users)



@app.route('/add_answer', methods=['GET','POST'])
@login_required
def add_answer():
    if 'answer' in request.values:
        # if request.form['question_id'] != None:
            # topics = Topic.query.all()
            question_id=request.form['question_id']
            # current_question=Topic.query.get(topic_id)
            new_answer = Answer()
            new_answer.answer_body = request.form['answer']
            new_answer.timestamp = datetime.utcnow()
            new_answer.question_id = int(question_id)
            new_answer.user_id = g.user.id
            db.session.add(new_answer)
            db.session.commit()
            flash ('Answer successfully added')

            answers = Answer.query.filter_by(question_id=question_id)
            current_question=Question.query.get(int(question_id))
            current_user = Users.query.get(int(current_question.user_id))
            users = Users.query.all()
            return render_template('template_answers.html',
                                   answers=answers,
                                   current_question=current_question,
                                   current_user=current_user,
                                   users=users)


@app.route('/votes')
@login_required
def votes():
    if 'answer_id' in request.values:

        question_id=request.values['question_id']
        answers = Answer.query.filter_by(question_id=question_id)
        current_question=Question.query.get(int(question_id))
        users = Users.query.all()

        answer_id=request.values['answer_id']
        current_answer=Answer.query.get(int(answer_id))
        current_answer.vote+=1
        db.session.add(current_answer)
        db.session.commit()
    return render_template('template_answers.html',
                           answers=answers,
                           current_question=current_question,
                           users=users)
