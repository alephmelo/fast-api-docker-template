from fastapi import FastAPI
from {{cookiecutter.app_name}}.utils.settings import Settings


app = FastAPI()
settings = Settings()


@app.get("/")
async def root():
    return {"message": f"Hello World, {settings.mode}"}
