import os

from .base import *  # noqa: F401,F403 - imported for gunicorn deployment

DEBUG = False

# ------------------------------------------------------------------------
# Site Configuration (PROD)
# ------------------------------------------------------------------------
SITE_NAME = "DigiDex"

SITE_PROTOCOL = "https"

WAGTAIL_SITE_NAME = SITE_NAME

WAGTAILADMIN_BASE_URL = f"{SITE_PROTOCOL}://{BASE_SITE_HOSTNAME}"

ALLOWED_HOSTS = [
    BASE_SITE_HOSTNAME,
    f"www.{BASE_SITE_HOSTNAME}"
]

# ------------------------------------------------------------------------
# Database Configuration (PROD)
# ------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DB_NAME = os.getenv('DB_NAME')

DB_USERNAME = os.getenv('DB_USERNAME')

DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_HOST = os.getenv('DB_HOST')

DB_PORT = os.getenv('DB_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT
    }
}

# ------------------------------------------------------------------------
# Common S3 Configuration (PROD)
# ------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = os.getenv("SPACES_ACCESS_KEY")

AWS_SECRET_ACCESS_KEY = os.getenv("SPACES_SECRET_KEY")

AWS_S3_REGION_NAME = os.getenv("SPACES_REGION_NAME")

AWS_S3_ENDPOINT_URL = f'{SITE_PROTOCOL}://{AWS_S3_REGION_NAME}.digitaloceanspaces.com'

AWS_S3_FILE_OVERWRITE = False

# Media Files S3 Configuration (PROD)
AWS_STORAGE_BUCKET_NAME_MEDIA = os.getenv("MEDIA_SPACES_BUCKET_NAME")

# Static Files S3 Configuration (PROD)
AWS_STORAGE_BUCKET_NAME_STATIC = os.getenv("STATIC_SPACES_BUCKET_NAME")

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
        'OPTIONS': {
            'access_key': AWS_ACCESS_KEY_ID,
            'secret_key': AWS_SECRET_ACCESS_KEY,
            'region_name': AWS_S3_REGION_NAME,
            'bucket_name': AWS_STORAGE_BUCKET_NAME_MEDIA,
            'endpoint_url': AWS_S3_ENDPOINT_URL,
            'default_acl': 'private',
            'querystring_auth': True,
            'file_overwrite': AWS_S3_FILE_OVERWRITE,
            'object_parameters': {
                'CacheControl': 'max-age=86400',
            },
        }
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
        'OPTIONS': {
            'access_key': AWS_ACCESS_KEY_ID,
            'secret_key': AWS_SECRET_ACCESS_KEY,
            'region_name': AWS_S3_REGION_NAME,
            'bucket_name': AWS_STORAGE_BUCKET_NAME_STATIC,
            'endpoint_url': AWS_S3_ENDPOINT_URL,
            'default_acl': 'public-read',
            'querystring_auth': False,
            'file_overwrite': AWS_S3_FILE_OVERWRITE,
            'object_parameters': {
                'CacheControl': 'max-age=86400',
            },
        }
    }
}

WAGTAIL_REDIRECTS_FILE_STORAGE = "cache"

# ------------------------------------------------------------------------
# Storage URL Configuration (PROD)
# ------------------------------------------------------------------------
MEDIA_URL = f'{SITE_PROTOCOL}://{AWS_STORAGE_BUCKET_NAME_MEDIA}.{AWS_S3_ENDPOINT_URL}/'

STATIC_URL = f'cdn.{BASE_SITE_HOSTNAME}/'

# ------------------------------------------------------------------------
# Storage Staticfiles Configuration (PROD)
# ------------------------------------------------------------------------
STATIC_ROOT = 'static/'

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ------------------------------------------------------------------------
# Search Configuration (PROD)
# ------------------------------------------------------------------------
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# ------------------------------------------------------------------------
# Email Configuration (PROD)
# ------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_SUBJECT_PREFIX = f"[{SITE_NAME}] "

EMAIL_HOST = os.getenv("EMAIL_HOST")

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

EMAIL_PORT = os.getenv("EMAIL_PORT")

EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ------------------------------------------------------------------------
# Authentication Configuration (PROD)
# ------------------------------------------------------------------------
ACCOUNT_EMAIL_SUBJECT_PREFIX = EMAIL_SUBJECT_PREFIX

# ------------------------------------------------------------------------
# Language Configuration (PROD)
# ------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', "English (United Kingdom)"),
    ('en-us', "English (United States)"),
    ('es', "Spanish (Spain)"),
    ('es-mx', "Spanish (Mexico)"),
]

USE_L10N = True

USE_I18N = True

# ------------------------------------------------------------------------
# Timezone Configuration (PROD)
# ------------------------------------------------------------------------
TIME_ZONE = "UTC"

USE_TZ = True

# ------------------------------------------------------------------------
# Session-based Security Configuration (PROD)
# ------------------------------------------------------------------------
SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")

CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

# ------------------------------------------------------------------------
# HTTP Strict Transport Security (HSTS) Configuration (PROD)
# ------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", SITE_PROTOCOL)

SECURE_HSTS_PRELOAD = True

DEFAULT_HSTS_SECONDS = 30 * 24 * 60 * 60  # 30 days

SECURE_HSTS_SECONDS = int(
    os.environ.get("SECURE_HSTS_SECONDS", DEFAULT_HSTS_SECONDS)
)  # noqa

# Do not use the `includeSubDomains` directive for HSTS. This needs to be prevented
# because the apps are running on client domains (or our own for staging), that are
# being used for other applications as well. We should therefore not impose any
# restrictions on these unrelated applications.
SECURE_HSTS_INCLUDE_SUBDOMAINS = False

# ------------------------------------------------------------------------
# Content Security Policy (CSP) Configuration (PROD)
# ------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

# Referrer-policy header settings.
REFERRER_POLICY = os.environ.get(  # noqa
    "SECURE_REFERRER_POLICY", "no-referrer-when-downgrade"
).strip()
