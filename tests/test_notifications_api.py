from unittest.mock import MagicMock

from fastapi.testclient import TestClient

from app.main import app
from app.core.database import get_db


client = TestClient(app)


def override_get_db():
    yield MagicMock()


app.dependency_overrides[get_db] = override_get_db

def test_create_notification_api():
    response = client.post(
        "/notifications/",
        json={
            "recipient_email": "test@example.com",
            "subject": "Test notification",
            "message": "Hello"
        }
    )

    print(response.json())