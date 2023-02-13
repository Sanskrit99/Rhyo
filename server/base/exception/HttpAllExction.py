
from fastapi import Request, HTTPException

class HttpAllExction:
    def __call__(self, request: Request, exc: HTTPException):
        return request

