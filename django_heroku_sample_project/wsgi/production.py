import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_heroku_sample_project.settings.production')

application = get_wsgi_application()