from pydantic_settings import BaseSettings


class HostSettings(BaseSettings):
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8051


host_settings = HostSettings()
