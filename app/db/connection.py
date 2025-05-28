from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///app/db/tv_service.db')

Base = declarative_base()

session = sessionmaker(bind=engine)()