from typing import Union
from loguru import logger
import sys

from fastapi import FastAPI

app = FastAPI(title="bug-tracker", debug=True)
logger.add(
    sys.stdout,
    colorize=True,
    level="DEBUG",
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
