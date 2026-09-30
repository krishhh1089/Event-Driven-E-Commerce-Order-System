from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.notification import NotificationCreate
from app.services import notification_service
from app.workers.tasks import send_notification


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

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

    send_notification.delay(new_notification.id)
    
    return {
        "message": "Notification created successfully",
        "notification_id": new_notification.id,
        "status": new_notification.status
    }
