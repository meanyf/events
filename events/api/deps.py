# deps.py

from fastapi import Depends
from sqlalchemy.orm import Session

from events.services.event_service import EventService
from events.repositories.event_repo import SqlEventRepo
from events.db.session import get_db


def get_event_service(
    db: Session = Depends(get_db),
) -> EventService:
    repo = SqlEventRepo(db)
    return EventService(repo)