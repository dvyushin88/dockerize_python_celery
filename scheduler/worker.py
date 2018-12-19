# -*- coding: utf-8 -*-

import os
from celery import Celery

env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL', 'redis://redis:6379')
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND', 'redis://redis:6379')

celery_worker = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)
