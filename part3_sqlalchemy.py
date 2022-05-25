from password import password
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
import pandas as pd

eng = create_engine(f"mysql+pymysql://root:{password}@localhost/car_rental")

tables = eng.execute("SHOW TABLES")
print(list(tables))
