# Copyright: (c) OpenSpug Organization. https://github.com/openspug/spug
# Copyright: (c) <spug.dev@gmail.com>
# Released under the AGPL-3.0 License.
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connections
from django_redis import get_redis_connection
from concurrent.futures import ThreadPoolExecutor
from apps.schedule.executors import schedule_worker_handler
from apps.monitor.executors import monitor_worker_handler
from apps.exec.executors import exec_worker_handler
from apps.notify.models import Notify
from threading import Thread
import logging
import time
import os
from ddtrace import patch, tracer

EXEC_WORKER_KEY = settings.EXEC_WORKER_KEY
MONITOR_WORKER_KEY = settings.MONITOR_WORKER_KEY
SCHEDULE_WORKER_KEY = settings.SCHEDULE_WORKER_KEY

os.environ["DD_SERVICE"] = "Python-App"    # 设置服务名
os.environ["DD_ENV"] = "Testing"          # 设置环境名
os.environ["DD_VERSION"] = "V1.1"         # 设置版本号
os.environ["DD_LOGS_INJECTION"] = "true"  # 开启log注入


FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')


logging.basicConfig(level=logging.WARNING, format=FORMAT)


class Worker:
    def __init__(self):
        self.rds = get_redis_connection()
        self._executor = ThreadPoolExecutor(max_workers=max(100, os.cpu_count() * 50))

    def job_done(self, future):
        connections.close_all()

    def queue_monitor(self):
        counter = 0
        while True:
            time.sleep((counter or 1) ** 3 * 10)
            qsize = self._executor._work_queue.qsize()
            if qsize > 0:
                if counter > 0:
                    content = '请检查监控、任务计划或批量执行等避免长耗时任务，必要时可重启服务清空队列。'
                    try:
                        Notify.make_system_notify(f'执行队列堆积（{qsize}）', content)
                    except Exception as e:
                        logging.warning(e)
                    finally:
                        connections.close_all()
                    logging.warning(f'!!! 执行队列堆积（{qsize}）')
                counter += 1
            else:
                counter = 0

    def run(self):
        logging.warning('Running worker')
        Thread(target=self.queue_monitor, daemon=True).start()
        self.rds.delete(EXEC_WORKER_KEY, MONITOR_WORKER_KEY, SCHEDULE_WORKER_KEY)
        while True:
            key, job = self.rds.blpop([EXEC_WORKER_KEY, SCHEDULE_WORKER_KEY, MONITOR_WORKER_KEY])
            key = key.decode()
            if key == SCHEDULE_WORKER_KEY:
                future = self._executor.submit(schedule_worker_handler, job)
            elif key == MONITOR_WORKER_KEY:
                future = self._executor.submit(monitor_worker_handler, job)
            elif key == EXEC_WORKER_KEY:
                future = self._executor.submit(exec_worker_handler, job)
            else:
                continue
            future.add_done_callback(self.job_done)


class Command(BaseCommand):
    help = 'Start worker process'

    def handle(self, *args, **options):
        w = Worker()
        w.run()
