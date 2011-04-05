import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_PATH, 'nsi_site.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'site_media')
MEDIA_URL = '/site_media'
#ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = 'orv%lcr5o-_@#uq+)@^krb)fh*_p$v*!xtayj4sly@d1s)r^1+'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

LETTUCE_AVOID_APPS = (
    'south',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'lettuce.django',
    'south',
    'apps.news',
    'apps.home_page',
    'apps.tools',
    'apps.projects',
    'apps.nsi_info',
    'apps.members',
)

