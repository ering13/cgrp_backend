# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, Boolean, Text
from sqlalchemy.orm import relationship
from .database import Base
from .models.user_roles import UserRole
from .models.roles import Role


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, index=True)
    device_status = Column(Boolean)
    username = Column(Text)
    first_name = Column(Text)
    last_name = Column(Text)
    password = Column(Text)
    roles = relationship(
        "Role",
        secondary=UserRole.__table__,
        backref="users"
    )

    device_data = relationship("DeviceData", back_populates="user", cascade="all, delete")
    symptoms = relationship("UserSymptoms", back_populates="user", cascade="all, delete")