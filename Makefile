install:
	pipenv --python python3.6
	pipenv install --dev

build:
	docker-compose build

up: down
	docker-compose up

down:
	docker-compose down -v --remove-orphans

shell:
	docker-compose run --rm web bash

run:
	pipenv run PYTHONPATH=. python manage.py runserver 0.0.0.0:8000

.PHONY=install up down run shell