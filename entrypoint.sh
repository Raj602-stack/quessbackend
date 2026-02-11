#!/bin/sh

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Creating superuser if not exists..."

python manage.py shell << END
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

print("DEBUG -> USERNAME:", username)
print("DEBUG -> EMAIL:", email)
print("DEBUG -> PASSWORD SET:", bool(password))

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superuser created.")
    else:
        print("Superuser already exists.")
else:
    print("Superuser environment variables missing!")
END

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
