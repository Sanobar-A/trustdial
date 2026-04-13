from sqlalchemy.orm import Session
from app.models.report import Report

def create_report(db: Session, business_id: int, report_type: str, comment: str = None):
    report = Report(
        business_id=business_id,
        report_type=report_type,
        comment=comment
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report


def get_reports(db: Session):
    return db.query(Report).all()