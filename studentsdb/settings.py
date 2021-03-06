"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PORTAL_URL = 'http://localhost:8000'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
"django.core.context_processors.request",
"studentsdb.context_processors.students_proc",
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
"django.core.context_processors.request",
)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm^+=bnoru74)tx2c11wproi47#ad+@gy^_#-#!mw*_8@v=*%0@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# We moved DATABASES variable to db.py module which added to .gitignore
# so we don't keep mysql passwords in repository
from .db import DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# email settings
# please, set here you smtp server details and your admin email
ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'accommodation.lviv@gmail.com'
EMAIL_HOST_PASSWORD = 'Q!w2E#r4T%'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
