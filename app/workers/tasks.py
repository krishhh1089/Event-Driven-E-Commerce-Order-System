from app.workers.celery_app import celery_app


@celery_app.task
def send_notification(notification_id: int):
    print(f"Processing notification {notification_id}")

    return {
        "notification_id": notification_id,
        "status": "processed"
    }