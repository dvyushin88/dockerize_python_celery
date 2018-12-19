# -*- coding: utf-8 -*-

import os
from redis import Redis

env = os.environ
INPUT_FOLDER = env.get('INPUT_FOLDER', '/celery-worker/input')
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
LIST_DIR_CACHE_KEY = 'i7gq9i7t8g4diyg487igb4k12'


redis = Redis(host=REDIS_HOST, port=6379)


def monitor_input_folder_for_changes(cache_time=10, txt_only=True):
    list_dir = os.listdir(INPUT_FOLDER)
    files_list = []

    if txt_only:
        list_dir = list(filter(lambda x: x.endswith('.txt'), list_dir))

    for fn in list_dir:
        cached = redis.get(fn)
        if not cached:
            files_list.append(fn)
            redis.set(fn, True, cache_time)

    return files_list
