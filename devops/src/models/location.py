from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import date

class Location(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    trip_id: UUID
    name: str
    country: str
    city: str
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    visit_date: Optional[date] = None