# -*- coding: utf-8 -*-

from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: int
    device_status: bool
    username: str
    first_name: str
    last_name: str
    password: str