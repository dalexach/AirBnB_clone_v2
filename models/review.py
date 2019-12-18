#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        __tablename__ : represents the table name
        place_id: place id
        user_id: user id
        text: review description
    """

    __tablename__ = "reviews"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_id = Column(String(1024), ForeignKey('places.id'),
                          nullable=False)
        user_id = Column(String(1024), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
