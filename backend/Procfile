web: gunicorn backend.wsgi
release: python manage.py migrate &&  python manage.py loaddata db.json

