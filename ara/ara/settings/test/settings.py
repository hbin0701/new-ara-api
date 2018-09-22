import datetime
import configparser

from ara.settings.settings import *


config = configparser.ConfigParser()

config.read(os.path.join(BASE_DIR, 'settings/test/config.cnf'))


DEBUG = True

SECRET_KEY = config.get('SECRET_KEY', 'secret_key')

ALLOWED_HOSTS = [
    '*',
]


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.get('DB', 'database'),
        'USER': config.get('DB', 'user'),
        'PASSWORD': config.get('DB', 'password'),
        'HOST': config.get('DB', 'host'),
        'PORT': config.get('DB', 'port'),
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
    },
}


# https://github.com/etianen/django-s3-storage/

AWS_REGION = 'ap-northeast-2'

AWS_ACCESS_KEY_ID = config.get('AWS', 'access_key_id')

AWS_SECRET_ACCESS_KEY = config.get('AWS', 'secret_access_key')

AWS_S3_BUCKET_AUTH = False

AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365

AWS_S3_BUCKET_NAME = 'new-ara-api-media-test'

AWS_S3_BUCKET_NAME_STATIC = 'new-ara-api-static-test'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

MEDIA_URL = 'https://s3.ap-northeast-2.amazonaws.com/new-ara-api-media-test/'

STATIC_URL = 'https://s3.ap-northeast-2.amazonaws.com/new-ara-api-static-test/'

DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'

STATICFILES_STORAGE = 'django_s3_storage.storage.StaticS3Storage'


# https://github.com/ottoyiu/django-cors-headers

CORS_ORIGIN_ALLOW_ALL = True


# http://getblimp.github.io/django-rest-framework-jwt/

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=SESSION_COOKIE_AGE),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(seconds=SESSION_COOKIE_AGE),
}


# http://www.django-rest-framework.org/

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'ara.classes.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


# https://wiki.sparcs.org/w/index.php/SPARCS_SSO

SSO_IS_BETA = False

SSO_CLIENT_ID = config.get('SPARCS_SSO', 'sso_client_id')

SSO_SECRET_KEY = config.get('SPARCS_SSO', 'sso_secret_key')
