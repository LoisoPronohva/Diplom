#!/bin/bash
set -e

# Ждём БД
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

# Миграции и статика
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Запуск сервера
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3