install:
	pip install pipenv
	pipenv --python python3.6
	pipenv install --dev

up:
	docker-compose up --build

run:
	pipenv run python manage.py runserver 0.0.0.0:8000

test:
	pipenv run py.test