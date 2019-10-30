#!/usr/bin/env bash
DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE:-production}
DJANGO_WSGI=${DJANGO_WSGI:-$(basename $(find . -maxdepth 2 -type f -name wsgi.py  | head -1|awk -F/ '{print $2"."$3}') .py)}

python manage.py collectstatic --no-input
python manage.py migrate
LOG_LEVEL=${LOG_LEVEL:-INFO}

printenv

/usr/local/bin/gunicorn --bind 0.0.0.0:5000 --log-level=${LOG_LEVEL} \
			${DJANGO_WSGI} $*
