
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi import Depends

from server.base.Cur import LoginModel
from server.base.depends.AuthDepends import AuthDepends
from server.base.request.SimpRequest import SimpRequest
from server.pack.XFragment import XFragment, SimpInjection, PrefixInjection


@PrefixInjection(prefix='/cand')
@SimpInjection(dependencies=[Depends(AuthDepends(LoginModel))])
class CandFragment(XFragment):
    def register_prefix(self, router: APIRouter):
        @router.post('/c0')
        async def t0(request: SimpRequest):
            return request.phuy.show()

        @router.websocket('/ws/{aka}/{ff}')
        async def ws(ws: WebSocket):
            pass
