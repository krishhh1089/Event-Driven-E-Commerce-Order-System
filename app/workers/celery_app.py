from celery import Celery

from app.core.config import settings


broker_url = (
    f"amqp://{settings.RABBITMQ_USER}:"
    f"{settings.RABBITMQ_PASSWORD}@"
    f"{settings.RABBITMQ_HOST}:"
    f"{settings.RABBITMQ_PORT}//"
)


celery_app = Celery(
    "notification_worker",
    broker=broker_url
)