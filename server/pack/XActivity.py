from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException

from server.base.config.ServerConfig import servcf
from server.base.exception.HttpAllExction import HttpAllExction
from server.base.exception.Validation import Validation
from server.base.middleware.ErrorMiddleware import ErrorMiddleware
import uvicorn


class XActivity:
    def __init__(self, app: FastAPI):
        self.app = app
        self._base()
        self.base()
        self._utils()
        self.utils()
        if servcf.http:
            pass
        else:
            uvicorn.run(app, host=servcf.host, port=servcf.port)

    def _base(self):
        self.__middleware()
        self.__exception()

    def __middleware(self):
        self.app.add_middleware(ErrorMiddleware)

    def __exception(self):
        self.app.add_exception_handler(RequestValidationError, Validation())
        self.app.add_exception_handler(HTTPException, HttpAllExction())

    def base(self):
        pass

    def _utils(self):
        pass

    def utils(self):
        pass
