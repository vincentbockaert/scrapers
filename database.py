from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from os import environ
from models import Base
from sqlalchemy_utils import create_database, database_exists

load_dotenv()

print(environ.get('DB_URI'))
if not database_exists(environ.get('DB_URI')):
    create_database(environ.get('DB_URI'))

engine = create_engine(environ.get('DB_URI'), echo=True)

Session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all(engine)