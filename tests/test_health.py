from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

from app.main import app
from sqlalchemy.exc import SQLAlchemyError


client = TestClient(app)


def test_health_check_database_connected():
    with patch("app.main.engine.connect") as mock_connect:
        mock_connection = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_connection

        response = client.get("/health")

        assert response.status_code == 200
        assert response.json() == {
            "status": "healthy",
            "database": "connected"
        }


def test_health_check_database_disconnected():
    with patch(
        "app.main.engine.connect",
        side_effect=SQLAlchemyError("Database unavailable")
    ):
        response = client.get("/health")

        assert response.status_code == 503
        assert response.json() == {
            "status": "unhealthy",
            "database": "disconnected"
        }