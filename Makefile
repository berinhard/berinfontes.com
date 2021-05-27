scss_watch:
	sass --watch project/static/sass/style.scss:project/static/css/style.css

migrate:
	python project/manage.py migrate

serve:
	python project/manage.py runserver
