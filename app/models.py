from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(150), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    questions = db.relationship('Question', backref = 'author', lazy = 'dynamic')
    answers = db.relationship('Answer', backref = 'answer', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' %(self.nickname)

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
    answers = db.relationship('Answer', backref = 'answer', lazy = 'dynamic')

    def __repr__(self):
        return '<Question %r>' %(self.question_body)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    answer_body =db.Column(db.String(180))
    answer_timestamp = db.Column (db.DateTime)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vote = db.Column (db.Integer, default = 0)

    def __repr__(self):
        return '<Question %r>' %(self.answer_body)