# -*- coding: utf-8 -*-

from pydantic import BaseModel

from typing import List
from backend.app.schemas.roles import RoleOut



class UserCreate(BaseModel):
    user_id: int
    device_status: bool
    username: str
    first_name: str
    last_name: str
    password: str
    roles: List[RoleOut] = []

    class Config:
        from_attributes = True