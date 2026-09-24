from pydantic import BaseModel, EmailStr


class NotificationCreate(BaseModel):
    recipient_email: EmailStr
    subject: str
    message: str