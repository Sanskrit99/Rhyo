
from fastapi import FastAPI

from server.pack.XMaster import XMaster


class Master(XMaster):
    def __init__(self, app: FastAPI):
        XMaster.__init__(self, app)

    def base(self):
        pass

    def utils(self):
        pass

    def fragment(self):
        from server.fragment.CandFragment import CandFragment
        from server.fragment.TestFragment import TestFragment
        from server.fragment.VideoFragment import VideoFragment
        return [
            TestFragment.instance(),
            CandFragment.instance(),
            VideoFragment.instance()
        ]
