release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn movieph.wsgi --log-file -