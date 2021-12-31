from .base import *

import django_heroku

SECRET_KEY = 'django-insecure--vsg-zph&$bj$_7t3&(6w6j6=sl_jl5+^u@dz3ha4e+5lw*=@6'

DEBUG = False

ALLOWED_HOSTS = ["django-heroku-sample-project.herokuapp.com"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'django_heroku_sample_project.wsgi.production.application'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())