#This contains our connections for our sqlalchemy to our postgress db


from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "postgresql+psycopg://<username>:<password>@<hostname>/<dbname>"

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Show SQL in logs
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
