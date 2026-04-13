from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    business_id = Column(Integer, ForeignKey("businesses.id"))
    report_type = Column(String)
    comment = Column(String)
