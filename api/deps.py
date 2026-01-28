# deps.py

from fastapi import Depends
from sqlalchemy.orm import Session

from services.event_service import EventService
from repositories.event_repo import SqlEventRepo
from db.session import get_db


def get_event_service(
    db: Session = Depends(get_db),
) -> EventService:
    repo = SqlEventRepo(db)
    return EventService(repo)