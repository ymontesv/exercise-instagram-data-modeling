import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    

class user(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    url = Column(String(50), nullable=False)
    post_id = Column(String(50), nullable=False)

class post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    
    
class comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(50), nullable=False)
    author_id = Column(String(50), nullable=False)
    Post_id = Column(Integer,ForeignKey(post.id))
     

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')