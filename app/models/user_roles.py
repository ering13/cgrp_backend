# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, ForeignKey
from app.database import Base

class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)



    role_id = Column(BigInteger, ForeignKey("roles.id"), primary_key=True)