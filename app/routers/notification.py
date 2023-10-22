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

@router.post("/edit/{notification_id}", description="Update a Notification")
async def update_notification(notification: Notification,notification_id:int=Path(...),cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
    try:
        resp = api.edit_notification(id_=notification_id, **notification.dict(exclude_unset=True))
    except UptimeKumaException as e:
        logging.info(e)
        raise HTTPException(404, {"message": "Notification not found !"})
    except TypeError as e:
        logging.error(e)
        raise HTTPException(422, str(e) )
    except Exception as e :
        logging.fatal(e)
        raise HTTPException(500, str(e))

    return {**resp, "notification_data":notification.dict(exclude_unset=True)}

@router.delete("delete/{notification_id}", description="Delete a specific notification")
async def delete_monitor(notification_id:int=Path(...) ,cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
    try:
        # kinda dumb the api doesnt check if th id exists he just sends an event
        resp = api.delete_notification(notification_id)
    except UptimeKumaException as e:
        logging.info(e)
        raise HTTPException(404, {"message": "Notification not found !"})
    except Exception as e :
        logging.fatal(e)
        raise HTTPException(500, str(e))

    return resp


@router.get("/notifications", description="Get all notification")
async def get_monitors(cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
    try :
        return {"notifications":  api.get_notifications()}
    except Exception as e :
        logging.fatal(e)
        raise HTTPException(500, str(e))

@router.get("/{notification_id}", description="Get Notification By ID")
async def get_monitor(notification_id:int=Path(...) , cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
 
    if notification_id :
        try:
            notification = api.get_notification(notification_id)
        except UptimeKumaException as e:
            logging.info(e)
            raise HTTPException(404, {"message": "notification not found !"})
        except Exception as e :
            logging.fatal(e)
            raise HTTPException(500, str(e))

        return {"notification": notification }

    raise HTTPException(404, {"message": "notification not found !"})


@router.post("/test-notification", description="Test Notification")
async def test_notification(notification: Notification , cur_user: API = Depends(get_current_user)):
    api: UptimeKumaApi = cur_user['api']
 
    try:
        resp = api.test_notification(**notification.dict())
    except TypeError as e:
        logging.error(e)
        raise HTTPException(422, str(e) )
    except Exception as e :
        logging.fatal(e)
        raise HTTPException(500, str(e))

    return resp

