from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
answer = Table('answer', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('answer_body', VARCHAR(length=180)),
    Column('answer_timestamp', DATETIME),
    Column('topic_id', INTEGER),
    Column('post_id', INTEGER),
    Column('user_id', INTEGER),
    Column('vote', INTEGER),
)

answer = Table('answer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('answer_body', String(length=180)),
    Column('answer_timestamp', DateTime),
    Column('topic_id', Integer),
    Column('question_id', Integer),
    Column('user_id', Integer),
    Column('vote', Integer, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['answer'].columns['post_id'].drop()
    post_meta.tables['answer'].columns['question_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['answer'].columns['post_id'].create()
    post_meta.tables['answer'].columns['question_id'].drop()
