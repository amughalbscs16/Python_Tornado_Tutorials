

from sqlalchemy import Column, Integer, String, MetaData, Table, ForeignKey

metadata = MetaData()

user_table = Table('user', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False),
    Column('email_address', String(60), key='email'),
    Column('password', String(60), key='email', nullable=True),
    Column('age', Integer, nullable=True)
)

medicine_table = Table('medicine', metadata,
    Column('medicine_id', Integer, primary_key=True),
    Column('medicine_name', String(60), nullable=False),
    Column('dosage_unit', String(10), nullable=True),
)





#

