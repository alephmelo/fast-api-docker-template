# FastAPI Docker

FastAPI Docker is a template to facilitate development as well productionization of your APIs. 

## Contents
- Docker
- Docker Compose
- FastAPI
- Development & Production infrastructure
- Makefile with shortcuts


## Customize
### Settings Files
The `envs` folder contains the files so you can use different settings depending on the environment you're running the API. It rellies on the enviroment variable `MODE`, which evals to `production` or `development` in order to read the correct `.env` file.

### Environment Variables
- `PORT`=`80`
- `HOST`=`0.0.0.0`
- `APP_MODULE`=`<module>.<module>:<fastapi-app-name>`
- `WORKERS_PER_CORE`=`1`

## Usage
### Download
```
$ cookiecutter https://github.com/alephmelo/fast-api-docker-template.git
```

### Build
This will build both `dev` and `prod` images.
```bash
$ make build
```

### Up
```bash
$ make up-dev
[...]
dev_1   | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
dev_1   | INFO:     Started reloader process [1] using statreload
dev_1   | INFO:     Started server process [7]
dev_1   | INFO:     Waiting for application startup.
dev_1   | INFO:     Application startup complete.
```

## Deployment
Just push your built image to whatever cloud provider or manually start the service. It's tagged locally as `<app_namme>/<app_name>:latest-prod`.

Example:
```
$ make up-prod
docker run -p 80:80 <app_namme>/<app_name>:latest-prod
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

## Release History
- 0.1.0 - Initial version.