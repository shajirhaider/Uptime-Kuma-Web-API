from fastapi import APIRouter, Depends, HTTPException, Path
from uptime_kuma_api import UptimeKumaApi, UptimeKumaException

from schemas.notification import Notification
from schemas.api import API
from utils.deps import get_current_user
from config import logger as logging


router = APIRouter(redirect_slashes=True)


@router.post("/add", description="Create a Notification")
async def create_notification(notification: Notification,cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
    try:
        resp = api.add_notification(**notification.dict())
    except TypeError as e:
        logging.error(e)
        raise HTTPException(422, str(e) )
    except Exception as e :
        logging.fatal(e)
        raise HTTPException(500, str(e))

    return resp

@router.get("/get", description="Create a Notification")
async def get_notification(cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
    try:
        resp = 'return notification'
    except TypeError as e:
        logging.error(e)
        raise HTTPException(422, str(e) )
    except Exception as e :
        logging.fatal(e)
        raise HTTPException(500, str(e))

    return resp
