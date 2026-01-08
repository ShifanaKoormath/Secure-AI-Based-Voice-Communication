from pydantic import BaseModel
from datetime import datetime


class MessageMetadata(BaseModel):
    message_id: str
    sender: str
    timestamp: datetime
    status: str  # SAFE | HARMFUL | URGENT
