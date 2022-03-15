from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Please populate your username, password and database_name
engine = create_engine('mysql+pymysql://ubuntu:ubuntu@localhost/pathis', echo=True)

Base = declarative_base()
