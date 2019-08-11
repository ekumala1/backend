from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    userid = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)

# class idk
