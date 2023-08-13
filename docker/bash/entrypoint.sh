#!/bin/bash

apt-get update

if [ "$1" = "run_django" ]; then
  python manage.py migrate --no-input
  python manage.py collectstatic --no-input --ignore admin
  exec gunicorn main.wsgi:application -b 0.0.0.0:8000 --reload --timeout 600
fi

if [ "$1" = "run_celery" ]; then
  python manage.py wait_for_db
  celery -A main worker -Q celery,products --autoscale=10,1 --loglevel=INFO -f celery.log
fi

exec "$@"