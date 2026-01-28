# event_repository.py

from typing import Protocol
from uuid import UUID
from domain.event import Event

class EventRepository(Protocol):
    def get(self, event_id: UUID) -> Event: ...
    def save(self, event: Event) -> None: ...