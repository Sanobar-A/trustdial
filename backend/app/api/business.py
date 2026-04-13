from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.business import BusinessCreate
from app.services.business_service import *
from app.services.queue_service import send_verification_task

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/business")
def create(business: BusinessCreate, db: Session = Depends(get_db)):
    return create_business(db, business)

@router.get("/businesses")
def get_all(db: Session = Depends(get_db)):
    return get_all_businesses(db)

@router.post("/business/{id}/verify")
def verify(id: int):
    send_verification_task(id)
    return {"message": "Task sent"}
