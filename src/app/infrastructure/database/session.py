from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATA_BASE_URL = ""

engine = create_engine(DATA_BASE_URL)

Session = sessionmaker(engine)

