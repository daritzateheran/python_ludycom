from pydantic import BaseModel, EmailStr
from typing import Optional

class Transaction(BaseModel):
    id: Optional[int]
    email: EmailStr
    lat: float
    lon: float    
    date: str