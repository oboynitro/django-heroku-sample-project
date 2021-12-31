from .base import *

import django_heroku

SECRET_KEY = 'django-insecure--vsg-zph&$bj$_7t3&(6w6j6=sl_jl5+^u@dz3ha4e+5lw*=@6'

DEBUG = True

ALLOWED_HOSTS = ["example-app.herokuapp.com"]

WSGI_APPLICATION = 'django_heroku_sample_project.wsgi.production.application'

django_heroku.settings(locals())