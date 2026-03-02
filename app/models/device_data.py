# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.users import User
from app.models.user_symptoms import UserSymptoms

class DeviceData(Base):
    __tablename__ = "device_data"

    device_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"))
    timestamp = Column(DateTime(timezone=True), nullable=False)
    value = Column(Float, nullable=False)

    user = relationship("User", back_populates="device_data")