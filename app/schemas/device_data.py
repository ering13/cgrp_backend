# -*- coding: utf-8 -*-

from pydantic import BaseModel
from datetime import datetime

class DeviceDataCreate(BaseModel):
    user_id: int
    timestamp: datetime
    value: float