#!/bin/bash

set -e

echo "Waiting for database..."

python manage.py migrate --noinput

echo "Collect static..."

python manage.py collectstatic --noinput

echo "Starting server..."

gunicorn config.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3