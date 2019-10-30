#!/bin/sh
cd $(dirname $0)
export PATH=${PWD}/.heroku/python/bin:${PATH}
./migrate.sh
python manage.py createsuperuser --no-input --username admin \
       --email ${DJANGO_SUPERUSER_EMAIL}
