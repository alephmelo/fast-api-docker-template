FROM python:{{cookiecutter.python_version}} as base

WORKDIR /home/{{cookiecutter.app_name}}

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

FROM base as development

COPY requirements_dev.txt requirements_dev.txt

RUN pip install -r requirements_dev.txt

FROM base as production

WORKDIR /production

COPY . .

ARG PORT=80
ARG HOST=0.0.0.0
ARG APP_MODULE={{cookiecutter.app_name}}.{{cookiecutter.main_file_name}}:app
ARG WORKERS_PER_CORE=1

ENV MODE=production
ENV APP_MODULE=${APP_MODULE}
ENV WORKERS_PER_CORE=${WORKERS_PER_CORE}}
ENV HOST=${HOST}
ENV PORT=${PORT}

EXPOSE ${PORT}

ENTRYPOINT [ "./scripts/start.sh" ]
