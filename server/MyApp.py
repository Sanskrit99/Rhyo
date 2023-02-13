#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 0:46
# @Author  : cap669
# @File    : MyApp.py
# @Software: PyCharm
from server.pack.XActivity import XActivity
from fastapi import FastAPI
from server.utils.Master import Master
class MyApp(XActivity):
    def __init__(self):
        app = FastAPI()
        XActivity.__init__(self, app)

    def base(self):
        pass

    def utils(self):
        self.master = Master(self.app)
