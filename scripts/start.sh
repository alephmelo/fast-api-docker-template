#! /usr/bin/env sh

exec uvicorn $APP_MODULE --port $PORT --host $HOST
