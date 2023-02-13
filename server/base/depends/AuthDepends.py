from server.base.Cur import LoginModel
from server.base.request.SimpRequest import SimpRequest, Phuy

from pydantic import BaseModel


class AuthModel(BaseModel):
    aka: str
    por: str


class AuthDepends:
    def __init__(self, model):
        self.__model:LoginModel = model

    def __call__(self, request: SimpRequest, auth: AuthModel) -> SimpRequest:
        request.phuy = Phuy()

        return request
