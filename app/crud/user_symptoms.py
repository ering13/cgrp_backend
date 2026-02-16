# -*- coding: utf-8 -*-

from sqlalchemy.orm import Session
from backend.app.models.user_symptoms import UserSymptoms

def create_symptom_data(db: Session, data):
    item = UserSymptoms(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
