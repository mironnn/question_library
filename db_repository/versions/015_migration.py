from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=50)),
    Column('email', VARCHAR(length=100)),
    Column('password', VARCHAR(length=15)),
    Column('registered_on', DATETIME),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=50)),
    Column('password', String(length=15)),
    Column('email', String(length=100)),
    Column('registered_on', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].drop()
    post_meta.tables['users'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].create()
    post_meta.tables['users'].drop()
