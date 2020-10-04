from os import getenv
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    mode: str
    dbpath: str

    class Config:
        env_file = f"workingtitle/envs/{getenv('MODE')}.env"
