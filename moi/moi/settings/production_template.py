from .base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moi',
        'USER': '',
        'PASSWORD': '',
    }
}

try:
    from .local import *
except ImportError:
    pass
