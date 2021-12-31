from .base import *

SECRET_KEY = 'django-insecure--vsg-zph&$bj$_7t3&(6w6j6=sl_jl5+^u@dz3ha4e+5lw*=@6'

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'django_heroku_sample_project.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}