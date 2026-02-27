from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASEE_URL = "sqlite:///./summary.db"

engine = create_engine(
    DATABASEE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()