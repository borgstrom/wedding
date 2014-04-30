from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wedding',
        'USER': 'wedding',
        'PASSWORD': 'wedding',
    }
}

DEBUG = True
TEMPLATE_DEBUG = True

STATIC_URL = "/static/"
STATIC_ROOT = project_dir("static")

MEDIA_URL = "/media/"
MEDIA_ROOT = project_dir("media")
