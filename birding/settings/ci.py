from . import *

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'ci',
       'USER': 'postgres',
       'PASSWORD': 'postgres',
       'HOST': 'postgres',
       'PORT': '5432',
   },
}
