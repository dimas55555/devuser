from sqlalchemy import Column, String, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

from src.db.base import Base


class UserORM(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    date_of_birth = Column(Date, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)