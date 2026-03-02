# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.database import Base
from .users import User


class UserSymptoms(Base):
    __tablename__ = "user_symptoms"

    id = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"))

    aura = Column(Boolean)
    nausea = Column(Boolean)
    user_input = Column(Text)
    payload = Column(JSONB)

    user = relationship("User", back_populates="symptoms")