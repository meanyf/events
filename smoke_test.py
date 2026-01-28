# smoke_test.py

from uuid import uuid4
from datetime import datetime, timezone

from domain.event import Event
from services.event_service import EventService
from services.interfaces.event_repository import EventRepository


class InMemoryEventRepo(EventRepository):
    def __init__(self):
        self.saved: list[Event] = []
        self.by_id: dict = {}

    def get(self, event_id):
        return self.by_id[event_id]

    def save(self, event: Event) -> None:
        self.saved.append(event)
        self.by_id[event.event_id] = event


def main():
    repo = InMemoryEventRepo()
    service = EventService(repo)

    user_id = uuid4()
    starts_at = datetime.now(timezone.utc)

    event = service.create(
        user_id=user_id,
        title="My event",
        starts_at=starts_at,
        lat=45.8150,
        lng=15.9819,
        address="Zagreb",
    )

    assert event.user_id == user_id
    assert event.title == "My event"
    assert len(repo.saved) == 1
    assert repo.saved[0].event_id == event.event_id

    print("OK: create() создал Event и сохранил в repo")


if __name__ == "__main__":
    main()
