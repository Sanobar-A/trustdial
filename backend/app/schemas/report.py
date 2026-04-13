from pydantic import BaseModel
from typing import Optional

class ReportCreate(BaseModel):
    business_id: int
    report_type: str
    comment: Optional[str] = None