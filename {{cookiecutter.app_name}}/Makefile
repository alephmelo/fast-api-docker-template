phony: build dev up-dev bash prod up-dev up-prod


build: dev prod

dev:
	docker-compose build dev

prod:
	docker-compose build prod

up-dev:
	docker-compose up dev

up-prod:
	docker run -p 80:80 {{cookiecutter.app_name}}/{{cookiecutter.app_name}}:latest-prod

bash:
	docker-compose run --entrypoint=bash dev
