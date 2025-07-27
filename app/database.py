from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
