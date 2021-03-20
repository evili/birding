import os
from django.conf import global_settings

DEBUG = False
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS',
                               '10.*,192.168.*,localhost,127.0.0.1,').replace(' ', '').split(',')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', global_settings.SECRET_KEY)


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE', 'django.db.backends.postgresql'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', os.environ.get('POSTGRES_HOST', 'postgres')),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', os.environ.get('POSTGRES_DB', 'django')),
        'USER': os.environ.get('DJANGO_DATABASE_USER', os.environ.get('POSTGRES_USER', 'django')),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', os.environ.get('POSTGRES_PASSWORD', 'django')),
    }
}

STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '/var/www/html/static')
MEDIA_ROOT = os.environ.get('DJANGO_STATIC_MEDIA', '/srv/www/html/media')
