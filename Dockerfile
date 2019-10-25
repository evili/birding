FROM python:3.7-alpine

ARG dev_packages="gcc g++ libc-dev libxml2-dev libxslt-dev postgresql-dev openldap-dev"

ADD . /srv
WORKDIR /srv

RUN pip install --upgrade pip
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

VOLUME ["/static", "/media"]

EXPOSE 8000/tcp

ENTRYPOINT ["./entrypoint.sh"]
