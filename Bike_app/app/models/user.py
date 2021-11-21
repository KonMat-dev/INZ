from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserLength():
    FIRST_NAME = 64
    SECOND_NAME = 64
    PHONE_NUMBER = 32
    EMAIL = 64
    DESCRIPTION = 2000


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    second_name = Column(String)
    phone_number = Column(String)
    password = Column(String)
    email = Column(String)
    description = Column(String)


    def __init__(self, first_name=None, second_name=None, phone_number=None, password=None, email=None,
                 description=None, disabled=False, username=None):

        self.first_name = first_name
        self.second_name = second_name
        self.phone_number = phone_number
        self.password = password
        self.email = email
        self.description = description
