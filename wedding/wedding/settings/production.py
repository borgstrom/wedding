import os

from .base import *

# allow 100Mb uploads
FILEBROWSER_MAX_UPLOAD_SIZE = 104857600

# Set our allowed hosts and mark that we want to use x-forwarded-host
# since we're running behind an nginx proxy
ALLOWED_HOSTS = [
    "rsvp.borgstrom.ca",
]
USE_X_FORWARDED_HOST = True

# Email settings
DEFAULT_FROM_EMAIL = "Borgstrom RSVP <rsvp@borgstrom.ca>"

# Admins & Managers
ADMINS = (
    ('Evan Borgstrom', 'evan@borgstrom.ca'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST']
    }
}


# Setup media as media.luminatofestival.com
# Store our media outside of our web directory
MEDIA_ROOT = "/home/weddingrsvp/media"
MEDIA_URL = "/media/"

# Setup static as static.luminatofestival.com
STATIC_ROOT = "/home/weddingrsvp/static"
STATIC_URL = "/static/"

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "/home/weddingrsvp/logs/application/production.log",
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
