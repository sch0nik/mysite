start:
	@poetry run gunicorn -b 192.168.1.200:8081 mysite.wsgi

start-dev:
	@poetry run python manage.py runserver

makemigration:
	@poetry run python manage.py makemigrations

migrate:
	@poetry run python manage.py migrate

upgrade:
	@git pull
