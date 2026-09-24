from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate

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
    try:
        new_notification = Notification(
            recipient_email=notification.recipient_email,
            subject=notification.subject,
            message=notification.message
        )

        db.add(new_notification)
        db.commit()
        db.refresh(new_notification)

        return {
            "message": "Notification created successfully",
            "notification_id": new_notification.id,
            "status": new_notification.status
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )