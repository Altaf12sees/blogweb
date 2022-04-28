import os
from pathlib import Path

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

hostname = os.environ['DBHOST']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['db-myblog'],
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'] + "@" + hostname,
        'PASSWORD': os.environ['110i5#ekwunC*'] 
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Enables whitenoise for serving static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False