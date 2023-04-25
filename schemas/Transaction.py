from pydantic import BaseModel, EmailStr
from typing import Optional

class Transaction(BaseModel):
    id: Optional[int]
    email: EmailStr
    lat: float
    lon: float    
    city: str
    date: str

class TransactionDb(BaseModel):
    id: Optional[int]
    idUser: EmailStr
    lat: float
    lon: float    
    date: str