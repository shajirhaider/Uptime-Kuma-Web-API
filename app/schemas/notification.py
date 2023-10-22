from typing import List, Optional
from pydantic import BaseModel


from uptime_kuma_api import  NotificationType


class Notification(BaseModel):

    # MQTT
    name: Optional[str] = None
    type: Optional[NotificationType] = None
    isDefault: Optional[str] = None
    telegramBotToken: Optional[str] = None
    telegramBotToken: Optional[str] = None
    telegramChatID: Optional[str] = None
    smtpBCC: Optional[str] = None
    smtpCC: Optional[str] = None
    smtpFrom: Optional[str] = None
    smtpHost: Optional[str] = None
    smtpPassword: Optional[str] = None
    smtpPort: Optional[str] = None
    smtpTo: Optional[str] = None
    smtpUsername: Optional[str] = None
    # state: Optional[str] = None


    class Config:
        use_enum_values = True

    
