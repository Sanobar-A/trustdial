from sqlalchemy import Column, Integer, String
from app.db.database import Base

class VerificationLog(Base):
    __tablename__ = "verification_logs"

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer)
    status_checked = Column(String)
    checked_at = Column(String)
