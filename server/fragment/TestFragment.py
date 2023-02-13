from server.base.depends.LoginDepends import LoginDepends, LoginModel
from server.base.depends.SimpDepends import SimpDepends, SimpRequest
from server.pack.XFragment import XFragment, PrefixInjection, SimpInjection
from fastapi import APIRouter
from fastapi import Depends

@PrefixInjection(prefix='/test')
@SimpInjection(dependencies=[Depends(SimpDepends())])
class TestFragment(XFragment):
    def register_prefix(self, router: APIRouter):
        @router.post('/t0')
        async def t0(request: SimpRequest):
            return request.phuy.show()

        @router.post('/login')
        async def login(request: SimpRequest = Depends(LoginDepends(LoginModel))):
            return request.phuy.show()


