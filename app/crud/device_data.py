# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session
from app.models.device_data import DeviceData

def create_device_data(db: Session, data):
    item = DeviceData(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item