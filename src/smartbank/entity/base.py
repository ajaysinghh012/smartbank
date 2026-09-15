from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

engine = create_engine("postgresql+psycopg2://postgres:@localhost:5432/smartbank", echo=True)

