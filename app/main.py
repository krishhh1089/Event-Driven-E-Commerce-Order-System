from fastapi import FastAPI
from app.api.notifications import router as notification_router

from app.core.database import engine
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI(
    title="Event Notification System",
    description="An event-driven notification backend",
    version="1.0.0"
)

app.include_router(notification_router)

@app.get("/")
def home():
    return {
        "message": "Event Notification System is running!"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except SQLAlchemyError:
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "database": "disconnected"
            }
        )