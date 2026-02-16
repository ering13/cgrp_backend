# -*- coding: utf-8 -*-

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SymptomCreate(BaseModel):
    user_id: int
    timestamp: datetime
    aura: Optional[bool]
    nausea: Optional[bool]
    user_input: Optional[str]
    payload: Optional[dict]