from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

db_url = "postgresql+psycopg2://postgres:sports@localhost:5432/prom"

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
