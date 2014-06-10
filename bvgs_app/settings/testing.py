from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'bvgs_app',                      # Or path to database file if using sqlite3.
    'USER': 'starter',
    'PASSWORD': 'password',
    'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    'PORT': '',                      # Set to empty string for default.
}
