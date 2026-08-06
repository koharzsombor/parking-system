import os
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

DATA_BASE_URL = os.getenv("DATABASE_URL")

engine: Engine = create_engine(DATA_BASE_URL)

SessionLocal: sessionmaker[Session] = sessionmaker(bind=engine, autoflush=False)

