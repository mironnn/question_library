from app import db
from datetime import datetime

# ROLE_USER = 0
# ROLE_ADMIN = 1

class User(db.Model):
    # __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index = True, unique = True)
    password = db.Column(db.String(15))
    email = db.Column(db.String(100), index = True, unique = True)
    # role = db.Column(db.SmallInteger, default = ROLE_USER)
    questions = db.relationship('Question', backref = 'author', lazy = 'dynamic')
    answers = db.relationship('Answer', backref = 'answer', lazy = 'dynamic')
    registered_on = db.Column(db.DateTime)

    # def __init__(self, username, password, email):
    #     self.username = username
    #     self.password = password
    #     self.email = email
    #     self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' %(self.username)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    topic_name = db.Column(db.String(80))

    def __repr__(self):
        return '<Topic %r>' %(self.topic_name)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    question_body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # answers = db.relationship('Answer', backref = 'answer', lazy = 'dynamic')

    def __repr__(self):
        return '<Question %r>' %(self.question_body)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    answer_body =db.Column(db.String(180))
    answer_timestamp = db.Column (db.DateTime)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vote = db.Column (db.Integer, default = 0)

    def __repr__(self):
        return '<Question %r>' %(self.answer_body)