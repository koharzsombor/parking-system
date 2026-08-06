from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

DATA_BASE_URL = ""

if DATA_BASE_URL == "":
    raise NotImplementedError("Database URL is not set up")

engine: Engine = create_engine(DATA_BASE_URL)

SessionLocal: sessionmaker[Session] = sessionmaker(engine)

