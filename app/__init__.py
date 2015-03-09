from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# from flask.ext.admin import Admin
# from flask.ext.admin.contrib.sqlamodel import ModelView

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models
# from models import User, Question

# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Question, db.session))