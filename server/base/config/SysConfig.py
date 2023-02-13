import os
from functools import lru_cache
from server.base.Tag import Ta


@lru_cache()
def register_env() -> str:
    os.environ.setdefault(Ta.env, Ta.dev)
    return os.environ.get(Ta.env, Ta.dev).lower()


env = register_env()
