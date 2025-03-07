import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

Base = declarative_base()

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False, index=True)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())



# SQLite database setup
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(engine)
