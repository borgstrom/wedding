"""
Django settings for wedding project.

Settings configured in this file will affect all of your different environment
(ie. production, dev, etc). If you want to target a specific environment make
your changes to the corresponding file in the settings directory.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: project_dir("subfolder", ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
project_dir = lambda *path: os.path.join(BASE_DIR, *path)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'UObTPdjjyvsfk8nRQ1sM5gaFd2dkyZh704NiNerDHgGN9AXOUMcO5R7OxVLfc6RxgDXT8ZDeql9TVPnWkNFX3tut3mH1F2rm'

DEBUG = False
TEMPLATE_DEBUG = False

# SECURITY WARNING: this needs to be setup in production
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'ui',
    'south',
    'wedding',
    'compressor',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wedding.urls'
WSGI_APPLICATION = 'wedding.wsgi.application'


# Database - Configure this in your environment settings file
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
