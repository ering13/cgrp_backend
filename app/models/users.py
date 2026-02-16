# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, Boolean, Text
from sqlalchemy.orm import relationship
from backend.app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True)
    device_status = Column(Boolean)
    username = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    password = Column(Text)

    device_data = relationship("DeviceData", back_populates="user", cascade="all, delete")
    symptoms = relationship("UserSymptoms", back_populates="user", cascade="all, delete")