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
