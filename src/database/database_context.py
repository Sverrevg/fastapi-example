import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("CONN_STRING")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare schema below:
metadata = MetaData("public")
Base = declarative_base(metadata=metadata)


# Dependency for db connection:
def get_db():  # type: ignore
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
