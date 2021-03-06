install:
	pipenv --python python3.6
	pipenv install --dev

up: down
	docker-compose up

down:
	docker-compose down

shell:
	docker-compose exec web bash

run:
	pipenv run PYTHONPATH=. python manage.py runserver 0.0.0.0:8000

.PHONY=install up down run 