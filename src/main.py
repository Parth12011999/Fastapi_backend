from fastapi import FastAPI, Request
from .database.core import engine, Base
from .api import register_routes
from .logging import configure_logging, LogLevels
from .exceptions import AppBaseException
from .response import ResponseService

configure_logging(LogLevels.info)

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.exception_handler(AppBaseException)
async def app_base_exception_handler(request: Request, exc: AppBaseException):
    return ResponseService.error(data=exc.data, message=exc.detail)


register_routes(app)
