from typing import List, Optional
from pydantic import BaseModel


from uptime_kuma_api import  NotificationType


class Notification(BaseModel):

    # MQT
    name: str
    type: NotificationType
    isDefault: Optional[bool] = False
    telegramBotToken: Optional[str] = None
    telegramSendSilently: Optional[bool] = False
    telegramChatID: Optional[str] = None
    telegramMessageThreadID :  Optional[str] = None
    smtpBCC: Optional[str] = None
    smtpCC: Optional[str] = None
    smtpFrom: Optional[str] = None
    smtpHost: Optional[str] = None
    smtpPassword: Optional[str] = None
    smtpPort: Optional[int] = None
    smtpTo: Optional[str] = None
    smtpUsername: Optional[str] = None
    # state: Optional[str] = None


    class Config:
        use_enum_values = True

    
