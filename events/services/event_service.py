# event_service.py
from uuid import uuid4
from events.domain.event import Event
from events.services.interfaces.event_repository import EventRepository

class EventService:
    def __init__(self, repo: EventRepository):
        self._repo = repo

    def create(self, user_id, title, starts_at, lat, lng, address, media_id=None, description=None):
        event = Event(
            event_id=uuid4(),
            user_id=user_id,
            title=title,
            starts_at=starts_at,
            lat=lat,
            lng=lng,
            address=address,
            media_id=media_id,
            description=description,
        )
        self._repo.save(event)
        return event