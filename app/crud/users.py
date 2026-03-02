# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session
from app.models.users import User

def create_user(db: Session, data):
    item = User(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item