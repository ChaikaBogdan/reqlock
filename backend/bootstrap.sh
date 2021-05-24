rm -f db.sqlite3 || true
find . -path "./reqlock/migrations/*.py" -not -name "__init__.py" -delete
find . -path "./reqlock/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --username admin  --email admin@reqlock.com
python manage.py collectstatic --noinput
(test -f db.json && python manage.py loaddata db.json) || true
python manage.py runserver
