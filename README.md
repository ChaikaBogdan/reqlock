# reqlock-backend
* `python manage.py collectstatic --noinput` - to create static files
* `python manage.py runserver` - to run dev server
* `python -m pip install -U pip wheel setuptools pipenv`
* `pipenv sync`
* `./loaddata.sh` - to import DB from db.json
* `./dumpdata.sh` - to export DB to db.json
* `./resetdb.sh` - to delete local db.sqlite, reset migrations and superuser
