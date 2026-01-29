# event.py
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID


class EventStatus(Enum):
    ACTIVE = "active"
    ENDED = "ended"


@dataclass
class Event:
    event_id: UUID
    user_id: UUID

    title: str
    starts_at: datetime

    lat: float
    lng: float
    address: str

    media_id: UUID | None = None
    description: str | None = None

    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    status: EventStatus = EventStatus.ACTIVE

    def end(self) -> None:
        if self.status == EventStatus.ENDED:
            raise ValueError("Event already ended")

        self.status = EventStatus.ENDED