#!/usr/bin/env python3
"""
User model definition
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    User class that represents the 'users' table
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

# Example to check the table structure


if __name__ == "__main__":
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))
