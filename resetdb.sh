rm db.sqlite3
find . -path "./reqlock/migrations/*.py" -not -name "__init__.py" -delete
find . -path "./reqlock/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --username admin  --email admin@reqlock.com
python manage.py runserver



