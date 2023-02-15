from pydantic import BaseSettings

from functools import lru_cache

from root.config.SysConfig import env


class ServerConfig(BaseSettings):
    host: str
    port: int
    http:bool

class PorServerConfig(ServerConfig):
    host = '127.0.0.1'
    port = 8886
    http = True


class DevServerConfig(ServerConfig):
    host = '127.0.0.1'
    port = 8886
    http = False
@lru_cache()
def register_config() -> ServerConfig:
    return dict(
        dev=DevServerConfig,
        por=PorServerConfig,
    )[env]()


servcf = register_config()