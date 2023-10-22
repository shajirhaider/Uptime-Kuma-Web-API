# main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers import (
    statuspage,
    monitor,
    auth,
    tags,
    cert,
    info,
    uptime,
    ping,
    database,
    user,
    settings,
    maintenance,
    notification
)
from config import settings as app_settings, logger
from app_setup import initialize_app

app = FastAPI(title=app_settings.PROJECT_NAME)
app.router.redirect_slashes = True

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(settings.router, prefix="/settings", tags=["Settings"])
app.include_router(database.router, prefix="/database", tags=["DataBase"])
app.include_router(monitor.router, prefix="/monitors", tags=["Monitor"])
app.include_router(statuspage.router, prefix="/statuspages", tags=["Status Page"])
app.include_router(maintenance.router, prefix="/maintenance", tags=["Maintenance"])
app.include_router(tags.router, prefix="/tags", tags=["Tags"])
app.include_router(cert.router, prefix="/cert_info", tags=["Certification Info"])
app.include_router(info.router, prefix="/info", tags=["Informations"])
app.include_router(ping.router, prefix="/ping", tags=["Ping Average"])
app.include_router(uptime.router, prefix="/uptime", tags=["Uptime"])
app.include_router(auth.router, prefix="/login", tags=["Authentication"])
app.include_router(notification.router, prefix="/notification", tags=["Notification"])


@app.on_event("startup")
async def startup_event():
    await initialize_app(app)
    logger.info("KumaAPI started...")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
