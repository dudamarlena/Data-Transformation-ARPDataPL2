from password import password
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
import pandas as pd

engine = create_engine(f"mysql+pymysql://root:{password}@localhost/car_rental")

tables = engine.execute("SHOW TABLES")

columns = engine.execute("SHOW COLUMNS FROM clients;")

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), default='Unknown')


# Base.metadata.create_all(engine)

print(list(engine.execute("SHOW TABLES")))
