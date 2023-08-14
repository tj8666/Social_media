from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

#connection = psycopg2.connect(user=postgres, password=123, host=localhost,database=social_media)

SQLALCHEMY_DATABASE_URI='postgresql://postgres:123@localhost/social_media'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from database.models import *

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
