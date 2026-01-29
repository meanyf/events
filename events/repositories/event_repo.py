# event_repo.py

from uuid import UUID
from sqlalchemy.orm import Session

from events.domain.event import Event, EventStatus
from events.services.interfaces.event_repository import EventRepository
from events.db.models import EventORM


class SqlEventRepo(EventRepository):
    def __init__(self, session: Session):
        self._session = session

    def get(self, event_id: UUID) -> Event:
        row = self._session.get(EventORM, event_id)
        if row is None:
            raise KeyError(f"Event not found: {event_id}")

        return Event(
            event_id=row.event_id,
            user_id=row.user_id,
            title=row.title,
            starts_at=row.starts_at,
            lat=row.lat,
            lng=row.lng,
            address=row.address,
            media_id=row.media_id,
            description=row.description,
            created_at=row.created_at,
            status=EventStatus(row.status),
        )

    def save(self, event: Event) -> None:
        row = self._session.get(EventORM, event.event_id)

        if row is None:
            row = EventORM(event_id=event.event_id)
            self._session.add(row)

        row.user_id = event.user_id
        row.title = event.title
        row.starts_at = event.starts_at
        row.lat = event.lat
        row.lng = event.lng
        row.address = event.address
        row.media_id = event.media_id
        row.description = event.description
        row.created_at = event.created_at
        row.status = event.status.value

        self._session.commit()
