from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': BASE_DIR.child('dev.db'),                      # Or path to database file if using sqlite3.
}

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False