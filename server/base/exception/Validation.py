
from fastapi import Request
from fastapi.exceptions import RequestValidationError

from server.base.response.ExcResponse import ParameterException


class Validation:
    def __call__(self, request: Request, exc: RequestValidationError):
        return ParameterException()
