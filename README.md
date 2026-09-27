# Event-Driven E-Commerce Order System

This project is a lightweight backend for managing order-related notifications in an event-driven architecture. It uses FastAPI, SQLAlchemy, PostgreSQL, RabbitMQ, Celery, and Alembic to provide a foundation for creating and processing notifications asynchronously.

## Overview

The current application includes:

- A FastAPI service with health and notification endpoints
- SQLAlchemy-backed persistence for notification records
- PostgreSQL as the primary data store
- RabbitMQ and Celery for async task processing
- Alembic migrations for schema updates
- Docker Compose for local infrastructure services

This is a backend foundation for an event-driven commerce workflow and is designed to be extended with order events, message dispatch logic, and downstream integrations.

## Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- PostgreSQL
- RabbitMQ
- Celery
- Alembic
- Docker Compose

## Project Structure

```text
.
├── alembic/                         # Alembic migration scripts
│   └── versions/
├── app/
│   ├── api/
│   │   └── notifications.py        # Notification API routes
│   ├── core/
│   │   ├── config.py               # Settings and environment configuration
│   │   └── database.py             # SQLAlchemy engine/session configuration
│   ├── models/
│   │   └── notification.py         # Notification table model
│   ├── schemas/
│   │   └── notification.py         # Pydantic request schema
│   ├── services/
│   │   └── notification_service.py # Notification creation logic
│   ├── workers/
│   │   ├── celery_app.py           # Celery app configuration
│   │   └── tasks.py                # Worker task definitions
│   ├── main.py                     # FastAPI application entry point
│   └── __init__.py
├── tests/
│   ├── test_health.py
│   ├── test_notification_service.py
│   └── test_notifications_api.py
├── .env                            # Local environment variables
├── .gitignore
├── alembic.ini                     # Alembic configuration
├── docker-compose.yml              # Postgres and RabbitMQ services
├── pytest.ini                     # Pytest configuration
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── .env.example                    # Optional example environment config (if present)
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.10+ installed
- Docker and Docker Compose installed
- A terminal such as PowerShell, Bash, or Command Prompt

## Environment Setup

Create a `.env` file in the project root with the following values:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5433/notification_db
ENVIRONMENT=development
RABBITMQ_USER=admin
RABBITMQ_PASSWORD=admin123
RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
```

The application reads these values from the environment through the settings class in `app/core/config.py`.

## Running the Project

### 1. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start infrastructure services

```bash
docker compose up -d
```

This starts:

- PostgreSQL on `localhost:5433`
- RabbitMQ on `localhost:5672`
- RabbitMQ management UI at `http://localhost:15672`

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Start the API server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- `http://localhost:8000/`
- `http://localhost:8000/health`
- `http://localhost:8000/notifications/`

### 6. Start the Celery worker

```bash
celery -A app.workers.celery_app worker --loglevel=info
```

This worker is configured to process async notification tasks using RabbitMQ.

## API Endpoints

### Health

- `GET /` — basic application welcome response
- `GET /health` — checks database connectivity and returns healthy/unhealthy status

### Notifications

- `POST /notifications/` — creates a notification record in the database

Example request:

```bash
curl -X POST "http://localhost:8000/notifications/" \
  -H "Content-Type: application/json" \
  -d '{
    "recipient_email": "user@example.com",
    "subject": "Order update",
    "message": "Your order has been shipped."
  }'
```

Example response:

```json
{
  "message": "Notification created successfully",
  "notification_id": 1,
  "status": "pending"
}
```

## Database Model

The notification model is defined in `app/models/notification.py` and includes:

- `id`
- `recipient_email`
- `subject`
- `message`
- `status` (default: `pending`)
- `created_at`

## Celery Worker

The Celery app is configured in `app/workers/celery_app.py` and uses RabbitMQ as the message broker. Task definitions live in `app/workers/tasks.py` and can be extended to include message dispatch, email sending, or integration with external systems.

## Tests

The project includes basic API and service tests under the `tests/` directory. Run them with:

```bash
pytest
```

## Notes

This repository is a foundational implementation for an event-driven notification system. It is set up for extension into a fuller commerce platform lifecycle, including order events, customer notifications, and asynchronous handling of outbound communication.

## License

This project does not currently declare a license. If needed, add a license file and update this section before production use.
