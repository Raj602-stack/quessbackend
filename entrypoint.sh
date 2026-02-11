#!/bin/sh

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Ensuring superuser exists (hardcoded test)..."

python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "12345"

user, created = User.objects.get_or_create(username=username, defaults={"email": email})

user.set_password(password)
user.is_superuser = True
user.is_staff = True
user.save()

print("Superuser ensured (hardcoded).")
END

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
