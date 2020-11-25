from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.orm import sessionmaker
from model import Base
import asyncio
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def get_db_url():
    db_url = 'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(os.getenv('user'), os.getenv('passw'),
                                                                 os.getenv('host'), os.getenv('port'),
                                                                 os.getenv('database'))
    return db_url


def get_engine():
    db_url = get_db_url()
    engine = create_engine(db_url, echo=True)
    return engine


def reset_db():
    db_url = get_db_url()
    if database_exists(db_url):
        drop_database(db_url)
    create_db()


def create_db():
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)


async def create_db_tables():
    reset_db()
    engine = get_engine()
    Base.metadata.create_all(engine)


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
