from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate
from app.services import notification_service

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a notification
@router.post("/")
def create_notification(
    notification: NotificationCreate,
    db: Session = Depends(get_db)
):
    new_notification = notification_service.create_notifications(
        db,
        notification
    )

    return {
        "message": "Notification created successfully",
        "notification_id": new_notification.id,
        "status": new_notification.status
    }
