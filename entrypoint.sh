#!/usr/bin/env bash
PYTHON_ENV=${PYTHON_ENV:-$(pwd)/env}
source ${PYTHON_ENV}/bin/activate
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-iiiahelpdesk.settings.production}
DJANGO_WSGI=${DJANGO_WSGI:-$(basename $(find . -maxdepth 2 -type f -name wsgi.py  | head -1|awk -F/ '{print $2"."$3}') .py)}
DJANGO_GUNICORN_PORT=${DJANGO_GUNICORN_PORT:-8000}
set -e
python manage.py collectstatic --no-input
python manage.py migrate
LOG_LEVEL=${LOG_LEVEL:-INFO}

exec ${PYTHON_ENV}/bin/gunicorn --bind 0.0.0.0:${DJANGO_GUNICORN_PORT} --log-level=${LOG_LEVEL} \
			${DJANGO_WSGI} $*
