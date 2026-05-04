from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import get_settings
from src.db import entities

engine = create_engine(get_settings().DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()