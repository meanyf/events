# event.py

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class CreateEventRequest(BaseModel):
    title: str
    starts_at: datetime
    lat: float
    lng: float
    address: str
    media_id: UUID | None = None
    description: str | None = None


class EventResponse(BaseModel):
    id: str
    title: str
    starts_at: datetime
    lat: float
    lng: float
    address: str
