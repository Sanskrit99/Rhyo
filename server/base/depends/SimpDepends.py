from server.base.request.SimpRequest import SimpRequest,Phuy



class SimpDepends:
    def __call__(self,request:SimpRequest) -> SimpRequest:
        request.phuy = Phuy()
        return request

