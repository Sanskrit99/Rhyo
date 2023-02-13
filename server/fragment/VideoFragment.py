from server.base.depends.LoginDepends import LoginDepends, LoginModel
from server.base.depends.SimpDepends import SimpDepends, SimpRequest
from server.pack.XFragment import XFragment, PrefixInjection, SimpInjection
from fastapi import APIRouter,Depends
from starlette.responses import Response, FileResponse


@PrefixInjection(prefix='/video')
@SimpInjection(dependencies=[Depends(SimpDepends())])
class VideoFragment(XFragment):
    def register_prefix(self, router: APIRouter):
        @router.get('/{fileName}.m3u8')
        async def m3u8(request: SimpRequest,response:Response,fileName:str):
            response.headers["Content-Type"] = "application/x-mpegURL"
            return FileResponse(r'D:\Aoc\Python\Rhyo\example\video\base\m3u8\video\{}.m3u8'.format(fileName), filename=fileName)

        @router.get('/snad/{fileName}.ts')
        async def ts(request: SimpRequest,response:Response,fileName:str):
            response.headers["Content-Type"] = "application/x-mpegURL"
            return FileResponse(r'D:\Aoc\Python\Rhyo\example\video\base\m3u8\video\{}.ts'.format(fileName), filename=fileName)

        @router.get('/{fileName}.key')
        async def key(request: SimpRequest,response:Response,fileName:str):
            response.headers["Content-Type"] = "application/x-mpegURL"
            return FileResponse(r'D:\Aoc\Python\Rhyo\example\video\base\keyinfo\video\encrypt.key', filename=fileName)

