import os
from pathlib import Path
import environ
from django.contrib.messages import constants as message_constants

BASE_DIR = Path(__file__).resolve().parent.parent
env=environ.Env()
environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # My Apps
    'pages.apps.PagesConfig',
    'teams.apps.TeamsConfig',
    'cars.apps.CarsConfig',
    'contact.apps.ContactConfig',

    # 3rd Party Apps
    'django_cleanup',
    'admin_interface',
    'colorfield',
    'ckeditor',
    'django.contrib.admin',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DATABASE_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT=os.path.join(BASE_DIR,"staticfiles")

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static")
]

MEDIA_ROOT = os.path.join(BASE_DIR,"media")
MEDIA_URL  = "/media/"

EMAIL_HOST          = "smtp.gmail.com"
EMAIL_USE_TLS       = True
EMAIL_USE_SSL       = False
EMAIL_PORT          = 587
EMAIL_HOST_USER     = env("EMAIL_HOST")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'


MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
	            message_constants.ERROR: 'danger',}
SITE_ID = 1
if not DEBUG:
    AUTHENTICATION_BACKENDS = ['backends.email_backends.EmailBackend']

LOGIN_REDIRECT_URL='url_homepage'