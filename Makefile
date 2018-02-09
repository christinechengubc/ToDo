init: FORCE
	mv db.sqlite3 db.sqlite3.bak
	python manage.py makemigrations 
	python manage.py migrate
	python manage.py loaddata init.json
FORCE: