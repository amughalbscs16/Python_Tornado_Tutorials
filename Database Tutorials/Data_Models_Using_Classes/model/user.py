from sqlalchemy import Column, Integer, String
from base_engine import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    name = Column(String(10))
    address = Column(String(10))
    email = Column(String(10))
