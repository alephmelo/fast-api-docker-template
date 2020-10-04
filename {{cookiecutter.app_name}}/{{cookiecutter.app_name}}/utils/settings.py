from os import getenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{{cookiecutter.app_name}}"
    mode: str
    dbpath: str

    class Config:
        env_file = f"{{cookiecutter.app_name}}/envs/{getenv('MODE')}.env"
