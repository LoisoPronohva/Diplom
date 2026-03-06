run:
	docker compose up --build

migrate:
	docker compose run web python manage.py migrate

createsuperuser:
	docker compose run web python manage.py createsuperuser

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report