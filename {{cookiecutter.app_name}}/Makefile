phony: build dev test tests up-dev bash prod up-dev up-prod


build: dev prod test

dev:
	docker-compose build dev

prod:
	docker-compose build prod

test:
	docker-compose build test

tests:
	docker-compose run test

up-dev:
	docker-compose up dev

up-prod:
	docker run -p 80:80 {{cookiecutter.app_name}}/{{cookiecutter.app_name}}:latest-prod

bash:
	docker-compose run --entrypoint=bash dev
