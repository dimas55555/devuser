from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from src.models.location import Location

class Trip(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: date
    status: str = "available"
    price: float
    locations: List[Location] = []
    max_participants: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None