from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///db.db")
session_local = sessionmaker(bind=engine)

Base = declarative_base()