# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.schemas.device_data import DeviceDataCreate
from backend.app.schemas.user_symptoms import SymptomCreate
from backend.app.schemas.users import UserCreate
from backend.app.crud.device_data import create_device_data
from backend.app.crud.user_symptoms import create_symptom_data
from backend.app.crud.users import create_user
from backend.app.models.user_symptoms import UserSymptoms
from backend.app.models.device_data import DeviceData
from backend.app.models.users import User
from fastapi import APIRouter, WebSocket, Query
from backend.app.utils.ws_manager import manager
from fastapi import BackgroundTasks

router = APIRouter()

#@router.post("/device-data")
#def ingest_device_data(data: DeviceDataCreate, db: Session = Depends(get_db)):

@router.post("/users")
def ingest_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)    

@router.post("/user-symptoms")
def ingest_user_symptoms(data: SymptomCreate, db: Session = Depends(get_db)):
    return create_symptom_data(db, data)

@router.get("/users/{user_id}/timeline")
def get_timeline(user_id: int, db: Session = Depends(get_db)):
    device_rows = db.query(DeviceData).filter(DeviceData.user_id == user_id).all()
    symptom_rows = db.query(UserSymptoms).filter(UserSymptoms.user_id == user_id).all()
    
    # Merge and sort
    timeline = sorted(
        [
            {"type": "device", "timestamp": d.timestamp, "value": d.value} for d in device_rows
        ] + [
            {"type": "symptom", "timestamp": s.timestamp, "payload": s.payload} for s in symptom_rows
        ],
        key=lambda x: x["timestamp"]
    )
    return timeline

@router.get("/user-find")
def get_user_info(username: str, db: Session = Depends(get_db)):
    user_info = db.query(User).filter(User.username == username).all()
    return user_info

@router.websocket("/ws/device-data")
async def websocket_endpoint(websocket: WebSocket, user_id: int = Query(...)):
    await manager.connect(websocket, user_id)
    try:
        while True:
            await websocket.receive_text()
    except Exception:
        manager.disconnect(websocket, user_id)
        
@router.post("/device-data")
def ingest_device_data(
    data: DeviceDataCreate, 
    background_tasks: BackgroundTasks, 
    db: Session = Depends(get_db) # Automatically injected
    ):
    item = create_device_data(db, data)
    
    background_tasks.add_task(manager.broadcast, item.user_id, {
        "type": "device_data",
        "user_id": item.user_id,
        "timestamp": item.timestamp.isoformat(),
        "value": item.value
    })
    
    return item    