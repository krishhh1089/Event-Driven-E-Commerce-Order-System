from fastapi import FastAPI

app = FastAPI(
    title="Event Notification System",
    description="An event-driven notification backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Event Notification System is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }