from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio
user = "admin"
passw = 1234
host = "localhost"
port = 3301
database = "sql_alchemy_2"
db_url = 'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(user, passw, host, port, database)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String(10))
   address = Column(String(10))
   email = Column(String(10))

async def populate_customers():

    Cust1 = Customers()
    Cust1.name = "Ali"
    Cust1.name = "Ali Addr"
    Cust1.email = "Ali@Ali.c"

    session = get_session()
    session.add(Cust1)
    #session.flush()
    session.commit()

def get_engine():
    engine = create_engine(db_url, echo = True)
    return engine

async def create_db_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind = engine)
    session = Session()
    return session

asyncio.run(create_db_tables())

asyncio.run(populate_customers())

