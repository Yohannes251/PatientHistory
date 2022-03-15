from sqlalchemy import create_engine, Column, String, Integer, DateTime, Sequence
from datetime import datetime
from models import engine, Base


class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime) 
    name = Column(String(128), nullable=False)
    gender = Column(String(128), nullable=False)
    age = Column(String(128), nullable=False)
    phonenumber = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)

    def __init__(self, name, gender, age, phonenumber, city):
        self.created_at = datetime.today()
        self.name = name
        self.gender = gender
        self.age = age
        self.phonenumber = phonenumber
        self.city = city

Base.metadata.create_all(engine)
