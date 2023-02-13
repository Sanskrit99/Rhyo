from pydantic import BaseSettings

from server.base.config.SysConfig import env
from functools import lru_cache


class PsqlConfig(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 5432
    user: str = 'postgres'
    password: str = 'postgres'


class DevPsqlConfig(PsqlConfig):
    password = '1234'


class PorPsqlConfig(PsqlConfig):
    password = '123456'


@lru_cache()
def register_config() -> PsqlConfig:
    return dict(
        dev=DevPsqlConfig,
        por=PorPsqlConfig,
    )[env]()


psqlcf = register_config()
