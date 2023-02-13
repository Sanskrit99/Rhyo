from fastapi import FastAPI,APIRouter
from typing import List
class XMaster:
    def __init__(self,app:FastAPI):
        self.base()
        self.utils()
        [app.include_router(router) for router in self.fragment() if router is not None]

    def base(self):
        pass

    def utils(self):
        pass

    def fragment(self) -> List[APIRouter]:
        pass

