clean: clean-eggs clean-build
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

clean-eggs:
	@find . -name '*.egg' -print0|xargs -0 rm -rf --
	@rm -rf .eggs/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

deps:
	poetry install

test: deps
	poetry run pytest -vvv

build: test
	poetry build

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

pyformat:
	black .

update:
	poetry update

runserver:
	poetry run bookstock_backend/manage.py runserver 0.0.0.0:8000

createsuperuser:
	poetry run bookstock_backend/manage.py createsuperuser

migrate:
	poetry run bookstock_backend/manage.py migrate

makemigrations:
	poetry run bookstock_backend/manage.py makemigrations

devdb:
	sudo docker-compose -f docker-compose-devdb.yml up --build -d

stopdevdb:
	sudo docker-compose -f docker-compose-devdb.yml down


