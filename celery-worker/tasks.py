# -*- coding: utf-8 -*-

import os
from datetime import datetime
from celery import Celery


env = os.environ
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL', 'redis://redis:6379')
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND', 'redis://redis:6379')
INPUT_FOLDER = env.get('INPUT_FOLDER', '/celery-worker/input')
OUTPUT_FOLDER = env.get('OUTPUT_FOLDER', '/celery-worker/output')


celery = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)


@celery.task(name='tasks.file_processing')
def file_processing(file_name=''):
    now = datetime.now()
    f = open('{}/{}'.format(INPUT_FOLDER, file_name))
    lines = 0
    buf_size = 1024 * 1024
    read_f = f.read  # loop optimization

    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)

    info_file_name = file_name.split('.txt')[0] + '_info.txt'
    file = open('{}/{}'.format(OUTPUT_FOLDER, info_file_name), 'w')
    file.write('File processed name: %s \n' % file_name)
    file.write('File lines count: %d \n' % lines)
    file.write('File processed last datetime: %s \n' % now.strftime('%Y-%m-%d %H:%M:%S.%s'))
    file.close()
