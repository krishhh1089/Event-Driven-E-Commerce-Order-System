from unittest.mock import MagicMock

from app.schemas.notification import NotificationCreate
from app.services.notification_service import create_notifications


def test_create_notification():
    mock_db = MagicMock()

    notification = NotificationCreate(
        recipient_email="test@example.com",
        subject="Test",
        message="Hello"
    )

    result = create_notifications(mock_db, notification)

    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

    assert result.recipient_email == "test@example.com"
    assert result.subject == "Test"
    assert result.message == "Hello"