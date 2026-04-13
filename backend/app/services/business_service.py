from sqlalchemy.orm import Session
from app.models.business import Business

def create_business(db: Session, data):
    business = Business(**data.dict())
    db.add(business)
    db.commit()
    db.refresh(business)
    return business

def get_all_businesses(db):
    return db.query(Business).all()

def get_business(db, id):
    return db.query(Business).filter(Business.id == id).first()
