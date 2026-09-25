from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


def create_notifications(
    db: Session,
    notification: NotificationCreate
):
    """Create a new notification in the database."""
    new_notification = Notification(
        recipient_email=notification.recipient_email,
        subject=notification.subject,
        message=notification.message
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification