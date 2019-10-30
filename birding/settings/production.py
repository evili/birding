import os
import ldap
from django_auth_ldap.config import LDAPSearch
from django.conf import global_settings

from . import *

DEBUG = False
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS',
                               '10.*,localhost,127.0.0.1,').replace(' ', '').split(',')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

AUTHENTICATION_BACKENDS = global_settings.AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS.insert(0,'django_auth_ldap.backend.LDAPBackend')

AUTH_LDAP_SERVER_URI = os.environ.get('DJANGO_AUTH_LDAP_SERVER_URI',
                                     "ldap://localhost")

AUTH_LDAP_USER_DN_TEMPLATE = os.environ.get(
    'DJANGO_AUTH_LDAP_USER_DN_TEMPLATE',
    'uid=%(user)s,ou=People'
)

AUTH_LDAP_START_TLS = os.environ.get('DJANGO_AUTH_LDAP_START_TLS', True)

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DJANGO_DATABASE_ENGINE','django.db.backends.postgresql'),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', os.environ.get('POSTGRES_HOST', 'postgres')),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', os.environ.get('POSTGRES_DB', 'iiiaportal')),
        'USER': os.environ.get('DJANGO_DATABASE_USER', os.environ.get('POSTGRES_USER', 'iiiaportal')),
        'PASSWORD' : os.environ.get('DJANGO_DATABASE_PASSWORD', os.environ.get('POSTGRES_PASSWORD', 'iiiaportal')),
    }
}

STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT', '/var/www/html/static')
MEDIA_ROOT = os.environ.get('DJANGO_STATIC_MEDIA', '/srv/www/html/media')
