#!/bin/sh
cd $(dirname $0)
printenv
pwd
python manage.py collectstatic --no-input
python manage.py migrate --no-input
