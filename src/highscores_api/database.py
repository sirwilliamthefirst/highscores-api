import getpass
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import Score
import os


# Database connection parameters
host = "hopandzip.com"  # Change if your DB is not on localhost
database = "ninja"
user = "ninja"
password = "A1b2C3d4E5f6G7h8I9j0K" #getpass.getpass()
port = 8888

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(DATABASE_URL, echo=True)
SQLModel.metadata.create_all(engine)

# Function to create tables in the database
def create_db():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)
    print("Database tables created!")

def add_score(score : Score):
    with Session(engine) as session:
        session.add(score)
        session.commit()
        session.refresh(score)
    return score

def get_all_scores():
    with Session(engine) as session:
        scores = session.exec(select(Score)).all()
    return scores
