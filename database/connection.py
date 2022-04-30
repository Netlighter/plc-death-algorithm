from sqlalchemy import create_engine, text


engine = create_engine("postgresql+psycopg2://msidnyilewfuuq:7ae7b1f7883072cad244e50b1cf3d9bdddd872fa28c599156dd28b8118a627d1@ec2-34-194-73-236.compute-1.amazonaws.com:5432/dfphlmapvc3j3p")

def check_connection():
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'\n"))
        print(result.all())


from sqlalchemy.orm import declarative_base
Base = declarative_base()
