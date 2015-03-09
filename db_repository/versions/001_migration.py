from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
comment = Table('comment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('comment_body', String(length=180)),
    Column('comment_timestamp', DateTime),
    Column('topic_id', Integer),
    Column('post_id', Integer),
    Column('user_id', Integer),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('topic_id', Integer),
    Column('question_body', String(length=150)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

topic = Table('topic', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('topic_name', String(length=80)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comment'].create()
    post_meta.tables['question'].create()
    post_meta.tables['topic'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comment'].drop()
    post_meta.tables['question'].drop()
    post_meta.tables['topic'].drop()
