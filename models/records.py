"""
    This module defines the data model for the records of patient
"""

from sqlalchemy import create_engine, Column, String, Integer, DateTime, Sequence
from datetime import datetime
from models import engine, Base


class Records(Base):
    """This class defines the records model which corresponds to records table in database"""

    # Define table name used for this model
    __tablename__ = 'records'

    # Define the specifications of the columns of the table
    rid = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    cardno = Column(Integer) 
    doctorname = Column(String(128), nullable=False)
    labtests = Column(String(500), nullable=False)
    labresults = Column(String(500), nullable=False)
    diagnosis = Column(String(500), nullable=False)
    treatment = Column(String(500), nullable=False)
    prescription = Column(String(500), nullable=False)
    critical = Column(Integer)

    def __init__(self, cardno, doctorname, labtests, labresults, diagnosis, treatment, prescription, critical):
        """Initializes the records object which will be stored in the database"""
        self.created_at = datetime.today()
        self.cardno = cardno
        self.doctorname = doctorname
        self.labtests = labtests
        self.labresults = labresults
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.prescription = prescription
        self.critical = critical

Base.metadata.create_all(engine)
