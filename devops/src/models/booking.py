from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional

class Booking(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    trip_id: UUID
    status: str = "pending"
    booked_at: datetime = Field(default_factory=datetime.utcnow)
    paid_amount: Optional[float] = None
    payment_status: str = "pending"