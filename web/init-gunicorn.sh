python manage.py makemigrations detection
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn -b :8000 car_detection.wsgi
