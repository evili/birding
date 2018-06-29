import os
from . import *

#
# POSTGRES_PORT should be named POSTGRES_URL (or similar)
# Here we try to parse it and put (true) port and host
# on the corresponding vars.
#
from  urllib.parse  import urlparse

_DB_PORT = os.environ.get('POSTGRES_PORT', '5432')
_DB_PARSED =  urlparse(_DB_PORT)

if _DB_PARSED.netloc:
    # true url found
    _DB_PORT = _DB_PARSED.port
    _DB_HOST = _DB_PARSED.hostname
else:
    # not an url, suppose it's just a port number
    _DB_HOST = os.environ.get('POSTGRES_HOST', 'postgres'),

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB','test'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': _DB_HOST,
        'PORT': _DB_PORT,
   },
}


