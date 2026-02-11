#!/bin/sh

echo "Waiting for database..."
sleep 5

python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Starting server..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
