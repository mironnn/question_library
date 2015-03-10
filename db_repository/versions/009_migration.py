from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', pre_meta,
    Column('user_id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=50)),
    Column('email', VARCHAR(length=100)),
    Column('password', VARCHAR(length=15)),
    Column('registered_on', DATETIME),
)

user = Table('user', post_meta,
    Column('user_id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=50)),
    Column('email', String(length=100)),
    Column('password', String(length=15)),
    Column('registered_on', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].drop()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].create()
    post_meta.tables['user'].drop()
