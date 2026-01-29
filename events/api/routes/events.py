# events.py

from uuid import uuid4
from fastapi import APIRouter, Depends

from events.api.schemas.event import CreateEventRequest, EventResponse
from events.services.event_service import EventService
from events.api.deps import get_event_service

router = APIRouter(prefix="/events")

@router.post("/", response_model=EventResponse)
def create_event(
    data: CreateEventRequest,
    service: EventService = Depends(get_event_service),
):
    event = service.create(
        user_id=uuid4(),  # потом из auth
        title=data.title,
        starts_at=data.starts_at,
        lat=data.lat,
        lng=data.lng,
        address=data.address,
        media_id=data.media_id,
        description=data.description,
    )

    return EventResponse(
        id=str(event.event_id),
        title=event.title,
        starts_at=event.starts_at,
        lat=event.lat,
        lng=event.lng,
        address=event.address,
    )
