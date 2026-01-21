# event_service.py
from repositories.event_repo import EventRepository

class EventService:
    def __init__(self, repo: EventRepository):
        self._repo = repo