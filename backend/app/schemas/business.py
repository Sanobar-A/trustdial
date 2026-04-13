from pydantic import BaseModel

class BusinessCreate(BaseModel):
    name: str
    address: str
    phone_number: str
