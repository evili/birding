FROM python:3.7-alpine

ARG dev_packages="gcc g++ libc-dev libxml2-dev libxslt-dev postgresql-dev openldap-dev"


RUN mkdir -pv /app
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN apk update && \
    apk add bash \
    ${dev_packages} && \
    pip install gunicorn \
      psycopg2-binary psycopg2 mysql-connector \
      django-heroku whitenoise[brotli] && \
    pip install -r requirements.txt && \
    apk del ${dev_packages} && \
    rm -fr /root/.cache


ENV DJANGO_STATIC_ROOT=/static
ENV DJANGO_MEDIA_ROOT=/media

VOLUME ["/app", "/static", "/media"]

EXPOSE 5000/tcp

ENTRYPOINT ["/app/entrypoint.sh"]
