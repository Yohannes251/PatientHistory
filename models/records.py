import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import models

class records(patient):
    def __init__(self):
        self.doctor_name = Column(String(128), nullable=False)
        self.lab_tests = Column(String(128), nullable=False)
        self.lab_results = Column(String(128), nullable=False)
        self.diagnosis = Column(String(128), nullable=False)
        self.treatment = Column(String(128), nullable=False)
        self.prescription = Column(String(128), nullable=False)
