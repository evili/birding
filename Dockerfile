FROM python:3.6-alpine
RUN apk add --update \
        py-gunicorn
# RUN pip install gunicorn
