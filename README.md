# Reqlock

## Backend

- `python -m pip install -U pip wheel setuptools pipenv`
- `pipenv sync -d`
- `pipenv shell`
- `python manage.py dumpdata  > db.json --exclude allauth` - to export DB to fixture db.json
- `./bootstrap.sh` - to delete local db.sqlite, reset migrations and superuser, start api server, seed db with test data
- `autopep8 --in-place --aggressive --aggressive -r ./backend` - autolint before push

## Frontend

- `./bootstrap.sh`

## How to use
- `admin@reqlock.com / admin` for both UI and Admin panel
- add new organisation `http://127.0.0.1:8000/reqlock/organisation/add/`
- add few projects and link them together `http://127.0.0.1:8000/reqlock/project/add/`
- visit `http://localhost:8080/projects`
