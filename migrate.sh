#!/bin/sh
cd $(dirname $0)
export PATH=${PWD}/.heroku/python/bin:${PATH}
python manage.py collectstatic --no-input
python manage.py migrate --no-input
