from sqlalchemy import Column, Integer, String
from base_engine import Base


class Medicine(Base):

   __tablename__='medicines'
   medicine_id=Column(Integer, primary_key=True)
   medicine_name=Column(String(10))
   dosage_unit=Column(String(10))

