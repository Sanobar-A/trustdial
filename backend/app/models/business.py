from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    status = Column(String, default="unverified")
