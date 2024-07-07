from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()
import os

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database_name = os.getenv("DB_NAME")

# Create the database engine
engine = create_engine(
    f"postgresql://{username}:{password}@{host}:{port}/{database_name}"
)
Session = sessionmaker(bind=engine)

base = declarative_base()


def get_db():
    """To get the session to be active and to close after the db operation."""
    session = Session()
    try:
        yield session
    finally:
        session.close()


class Registration(base):
    __tablename__ = "registration"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)
    date_of_birth = Column(Date)
    Age = Column(Integer)
