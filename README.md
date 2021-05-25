# Reqlock

## Backend
* `python -m pip install -U pip wheel setuptools pipenv`
* `pipenv sync`
* `pipenv shell`
* `python manage.py dumpdata > db.json` - to export DB to fixture db.json
* `./bootstrap.sh` - to delete local db.sqlite, reset migrations and superuser, start api server
* To get db schema - install `graphviz` binary and run `python manage.py graph_models --pydot -a -g -o db_schema.png`


## Frontend
* `./bootstrap.sh`
