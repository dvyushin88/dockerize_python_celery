#!/usr/bin/env python

import sched
import time
from utils import monitor_input_folder_for_changes
from worker import celery_worker

CACHE_TIME = 120


def input_folder_scan():
    changed_files = monitor_input_folder_for_changes(cache_time=CACHE_TIME)

    for fn in changed_files:
        celery_worker.send_task(
            'tasks.file_processing',
            kwargs={'file_name': fn}
        )


def main(sc):
    try:
        input_folder_scan()
    except Exception as e:
        print('Scheduler app Exception:', e)
    s.enter(10, 1, main, (sc,))


if __name__ == '__main__':
    # sched is used to schedule main function every 10 seconds.
    s = sched.scheduler(time.time, time.sleep)
    s.enter(10, 1, main, (s,))
    s.run()
