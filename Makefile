phony: build dev up-dev bash prod up-dev up-prod


build: dev prod

dev:
	docker-compose build dev

prod:
	docker-compose build prod

up-dev:
	docker-compose up dev

up-prod:
	docker run -p 80:80 workingtitle/workingtitle:latest-prod

bash:
	docker-compose run --entrypoint=bash dev
