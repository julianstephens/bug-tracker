import sys

from fastapi import FastAPI, Security
from loguru import logger

from app.routes import api_router
from app.services.auth import check_auth

logger.add(
    sys.stdout,
    colorize=True,
    level="DEBUG",
)

app = FastAPI(title="bug-tracker", debug=True, dependencies=[Security(check_auth)])


@app.get("/api")
async def checkhealth():
    return {"message": "API healthy."}


app.include_router(api_router, prefix="/api")