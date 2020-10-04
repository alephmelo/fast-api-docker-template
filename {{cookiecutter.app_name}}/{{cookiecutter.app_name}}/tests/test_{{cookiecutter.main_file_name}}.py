from fastapi.testclient import TestClient

from {{cookiecutter.app_name}}.{{cookiecutter.main_file_name}} import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World, testing"}
