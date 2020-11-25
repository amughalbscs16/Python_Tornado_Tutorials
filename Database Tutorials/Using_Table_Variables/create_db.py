from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

import asyncio
Base = declarative_base()

from models_file import user_table, medicine_table, metadata
from sqlalchemy_utils import database_exists, create_database, drop_database


def get_db_url():
    user = "admin"
    passw = 1234
    host = "localhost"
    port = 3301
    database = "sql_alchemy_1"
    db_url = 'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(user, passw, host, port, database)
    return db_url

def get_db_connection():
    db_url = get_db_url()
    engine = create_engine(db_url)

    return engine

def reset_db():
    db_url = get_db_url()
    if database_exists(db_url):
        drop_database(db_url)
    create_db()

def create_db():
    engine = get_db_connection()
    if not database_exists(engine.url):
        create_database(engine.url)

def get_tables():
    tables = [user_table, medicine_table]
    return tables

def create_db_tables():
    engine = get_db_connection()
    engine.connect()
    tables = get_tables()

    for table in tables:
        table.create(engine)

reset_db()
create_db_tables()
