from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.report import ReportCreate
from app.models.report import Report

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/report")
def create_report(report: ReportCreate, db: Session = Depends(get_db)):
    new_report = Report(
        business_id=report.business_id,
        report_type=report.report_type,
        comment=report.comment
    )
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report

@router.get("/reports")
def get_reports(db: Session = Depends(get_db)):
    return db.query(Report).all()