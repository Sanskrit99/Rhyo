from fastapi import APIRouter, params
from typing import Optional, Sequence
from abc import ABC, abstractmethod


def PrefixInjection(prefix: str = None):
    def back(cls):
        cls.prefix = prefix
        return cls

    return back


def SimpInjection(dependencies: Optional[Sequence[params.Depends]] = None):
    def back(cls):
        cls.dependencies = dependencies
        return cls

    return back


class XFragment(ABC):
    prefix: str = None
    dependencies: Optional[Sequence[params.Depends]] = None
    router: APIRouter = None

    def __init__(self,
                 prefix: str = None,
                 dependencies: Optional[Sequence[params.Depends]] = None,
                 router: APIRouter = None,
                 *args, **kwargs):
        self._prefix = self.prefix or prefix
        self._dependencies = self.dependencies or dependencies
        self._router = self.router or router or APIRouter(
            prefix=self._prefix,
            dependencies=self._dependencies,
        )

    def build(self) -> APIRouter:
        self.register_prefix(router=self._router)
        return self._router

    @classmethod
    def instance(cls,
                 prefix: str = None,
                 dependencies: Optional[Sequence[params.Depends]] = None,
                 router: APIRouter = None,
                 *args, **kwargs
                 ):
        return cls(
            prefix,
            dependencies,
            router,
            *args, *kwargs
        ).build()

    @abstractmethod
    def register_prefix(self, router: APIRouter):
        pass
