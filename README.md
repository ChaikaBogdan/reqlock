# Reqlock

## Backend
* `python -m pip install -U pip wheel setuptools pipenv`
* `pipenv sync`
* `python manage.py dumpdata > db.json` - to import DB from db.json
* `./bootstrap.sh` - to delete local db.sqlite, reset migrations and superuser, start api server
* To get db schema - install `graphviz` binary and run `python manage.py graph_models --pydot -a -g -o db_schema.png`


## Frontend
* `./bootstrap.sh`
