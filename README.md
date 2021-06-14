# Reqlock

## Backend

- `python -m pip install -U pip wheel setuptools pipenv`
- `pipenv sync`
- `pipenv shell`
- `python manage.py dumpdata > db.json` - to export DB to fixture db.json
- `./bootstrap.sh` - to delete local db.sqlite, reset migrations and superuser, start api server
- `autopep8 --in-place --aggressive --aggressive -r .` - autolint before push

## Frontend

- `./bootstrap.sh`
