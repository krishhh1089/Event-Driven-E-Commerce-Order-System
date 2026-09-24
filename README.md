# Event-Driven E-Commerce Order System

A lightweight event-driven notification backend for an e-commerce platform. The project is built with FastAPI, SQLAlchemy, PostgreSQL, RabbitMQ, and Alembic, and is structured so it can process order-related events and send notifications asynchronously.

## Overview

This repository currently contains the foundational backend services for an event-driven notification system:

- FastAPI application for health and API endpoints
- SQLAlchemy models for persistence
- PostgreSQL database setup
- RabbitMQ message broker support for event-driven communication
- Alembic migrations for schema management

## Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- PostgreSQL
- RabbitMQ
- Alembic
- Docker Compose

## Project Structure

```text
.
├── alembic/                 # Database migration scripts
├── app/
│   ├── api/                # API routes and handlers
│   ├── core/               # Shared app configuration
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Request/response schemas
│   ├── services/           # Business logic and service layer
│   ├── workers/            # Background job / broker workers
│   ├── main.py             # FastAPI application entry point
│   └── test_db.py          # DB connectivity test helper
├── tests/                  # Test suite
├── .env                    # Local environment variables
├── alembic.ini             # Alembic configuration
├── docker-compose.yml      # PostgreSQL and RabbitMQ services
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Prerequisites

Before running the project, make sure you have:

- Python installed
- Docker and Docker Compose installed
- Access to a terminal or PowerShell

## Environment Setup

This project uses a local PostgreSQL database configured in `.env`:

```env
DATABASE_URL=postgresql://admin:admin123@localhost:5433/notification_db
```

## Running the Services

### 1. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL and RabbitMQ with Docker

```bash
docker compose up -d
```

This starts:

- PostgreSQL on `localhost:5433`
- RabbitMQ on `localhost:5672`
- RabbitMQ management UI at `http://localhost:15672`

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- `http://localhost:8000/`
- `http://localhost:8000/health`

## Current API Endpoints

The application currently exposes basic health endpoints:

- `GET /` — welcome message
- `GET /health` — health check status

## Database

The application uses SQLAlchemy with a declarative base model. The notification table is defined in `app/models/notification.py`.

### Notification model fields

- `id`
- `recipient_email`
- `subject`
- `message`
- `status`
- `created_at`

## Migrations

This project includes Alembic for database migrations.

```bash
alembic upgrade head
```

## Notes

This repository is in an early-stage foundation setup. The event-driven workflow, notification dispatch logic, and e-commerce integration points are planned to be built on top of the current PostgreSQL and RabbitMQ foundation.

## License

This project is currently unlicensed unless specified otherwise.
