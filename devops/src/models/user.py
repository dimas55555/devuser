from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict
from uuid import UUID, uuid4
from datetime import datetime, date

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: EmailStr
    password: str
    date_of_birth: Optional[date] = None
    preferences: Optional[Dict[str, str]] = {}
    payment_info: Optional[Dict[str, str]] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None