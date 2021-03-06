from datetime import timedelta
from os import environ as os_environ
from celery.schedules import crontab


# Redis
from ara.settings import TIME_ZONE

REDIS_HOST = os_environ.get('NEWARA_REDIS_ADDRESS', 'localhost')
REDIS_DATABASE = int(os_environ.get('NEWARA_REDIS_DATABASE', 0))
REDIS_URL = f'redis://{REDIS_HOST}:6379/{REDIS_DATABASE}'

CACHES_TIMEOUT = timedelta(days=14)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': CACHES_TIMEOUT,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Celery
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_WORKER_CONCURRENCY = os_environ.get('NEWARA_CELERY_CONCURRENCY')
CELERY_ACCEPT_CONTENT = ['json', 'pickle']  # datetime때문에 pickle 사용
CELERY_EVENT_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_TASK_RESULT_EXPIRES = int(os_environ.get('NEWARA_CELERY_EXPIRES', 600))


def create_scheduler_config(name, period=None, crontab=None):
    config = {'NAME': name, 'PING_URL': os_environ.get(f'NEWARA_{name}_PING_URL', None)}
    if period is not None:
        config['PERIOD'] = timedelta(seconds=int(os_environ.get(f'NEWARA_{name}_PERIOD', period)))
    if crontab is not None:
        config['CRONTAB'] = crontab
    return config


SCHEDULERS = {
    # 'CRAWL_PORTAL': create_scheduler_config('CRAWL_PORTAL', crontab=crontab(minute=0)),  # 매 0분 (1시간마다)
    'CRAWL_PORTAL': create_scheduler_config('CRAWL_PORTAL', crontab=crontab()),
}
