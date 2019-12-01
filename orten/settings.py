"""
Django settings for orten project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from environs import Env
import os

env = Env()
env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# Security
SECRET_KEY = env.str("SECRET_KEY")
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=True)
# добавляет preload директиву в заголовок
SECURE_HSTS_PRELOAD = env.bool('SECURE_HSTS_PRELOAD', default=True)
# добавляет includeSubDomains директиву в заголовок
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool('SECURE_CONTENT_TYPE_NOSNIFF', default=True)
SECURE_BROWSER_XSS_FILTER = env.bool('SECURE_BROWSER_XSS_FILTER', default=True)
# все не-HTTPS запросы на HTTPS
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
# Указывает использовать ли безопасные куки для сессии
SESSION_COOKIE_SECURE = env.bool('SESSION_COOKIE_SECURE', default=True)
# Указывает, использовать ли безопасные куки для CSRF.
CSRF_COOKIE_SECURE = env.bool('CSRF_COOKIE_SECURE', default=True)

X_FRAME_OPTIONS=env.str('X_FRAME_OPTIONS', default=True)

# Если URL удовлетворяет регулярному выражению из этого списка, запрос не будет перенаправлен По умолчанию: [] SECURE_SSL_REDIRECT=False
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))
SITE_ID = 1
APPEND_SLASH = True

# Application definition
INSTALLED_APPS = [
    # django-admin-tools
    'admin_tools' ,
    'admin_tools.theming' ,
    'admin_tools.menu' ,
    'admin_tools.dashboard' ,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django_dramatiq',
    'django_filters',
    'taggit',
    'mptt',
    'import_export',
    'debug_toolbar',
    'django_redis',
    'bootstrap4',
    'ckeditor',
    'watson',
    'modeltranslation',
    # 'modeltranslation_xliff',
    'shop',
    'cart',
    'order',
    'change_price',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # django-debug-toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # The Django Redirects App
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'orten.urls'
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'context_processors.cart.cart',
                'context_processors.category.category',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'admin_tools.template_loaders.Loader',
            ],
        },
    },
]

# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# DATABASES = {"default": env.dj_db_url("DATABASE_URL")}
DATABASES = {
    'default': {
        'ENGINE': env.str("DB_ENGINE"),
        'NAME': env.str("DB_NAME"),
        'USER': env.str("DB_USER"),
        'PASSWORD': env.str("DB_PASSWORD"),
        'HOST': env.str("DB_HOST"),
        'PORT': env.str("DB_PORT"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DECIMAL_SEPARATOR = "."
DATE_INPUT_FORMATS = ['%d.%m.%Y']
IMPORT_EXPORT_USE_TRANSACTIONS = True
WSGI_APPLICATION = 'orten.wsgi.application'

gettext = lambda s: s
LANGUAGES = (
    ('ru', gettext('Russian')),
    ('uk', gettext('Ukrainian')),
)

# LANGUAGES = (
#     ('ru', 'Russian'),
#     ('uk', 'Ukrainian'),
# )

 # указываем, где лежат файлы перевода
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Extra places for collectstatic to find static files.
STATIC_ROOT = env.str('STATIC_ROOT')
# STATIC_ROOT = '/home/orten/orten.in.ua/static/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_ROOT = env.str('MEDIA_ROOT')
# MEDIA_ROOT = '/home/orten/orten.in.ua/static/media'
MEDIA_URL = '/media/'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str("EMAIL_HOST")
EMAIL_PORT = env.int("EMAIL_PORT")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
ADMINS=[('Ivan', 'orten.in.ua@gmail.com'),]
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL")
# Асинхронность
DRAMATIQ_RESULT_BACKEND = {
    "BACKEND": "dramatiq.results.backends.redis.RedisBackend",
    "BACKEND_OPTIONS": {
        "url": "redis://127.0.0.1:6379",
    },
    "MIDDLEWARE_OPTIONS": {
        "result_ttl": 60000
    }
}

# Кєш и сессии
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Время ожидания сокета
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # in seconds
            # исключения поведения
            "IGNORE_EXCEPTIONS": True,
            # пул соединений
            "CONNECTION_POOL_KWARGS": {"max_connections": 128}
        }
    }
}
CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 7200 #Время жизни сессии секундах

# django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'RESULTS_CACHE_SIZE': 100,
    'SQL_WARNING_THRESHOLD': 2000
}