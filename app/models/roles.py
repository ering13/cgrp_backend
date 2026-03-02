# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, String
from .database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(BigInteger, primary_key=True)
    name = Column(String, unique=True, nullable=False)