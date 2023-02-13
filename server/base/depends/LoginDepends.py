from server.base.depends.SimpDepends import Phuy, SimpRequest
from pydantic import BaseModel


class LoginModel(BaseModel):
    us: str
    pw: str


class LoginDepends:
    def __init__(self, model):
        self.__model = model

    def __call__(self, request: SimpRequest, login: LoginModel) -> SimpRequest:
        request.phuy = Phuy()
        return request
