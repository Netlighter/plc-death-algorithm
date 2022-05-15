from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.getenv("DB_URL")

engine = create_engine(db_url)


def check_connection():
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'\n"))
        print(result.all())


from sqlalchemy.orm import declarative_base
Base = declarative_base()
Base.metadata.create_all(engine)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine))
session = Session()
