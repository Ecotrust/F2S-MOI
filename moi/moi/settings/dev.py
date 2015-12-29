from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%1sa7_bl3oqzcea7_47#rdlgaix111=eg+)&2alsqw80&874g$'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moi',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
    }
}

try:
    from .local import *
except ImportError:
    pass
