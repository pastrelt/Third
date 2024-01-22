# Базовой структурной единицей системы Celery является task (задача).
# Все задачи принято хранить в файлах с названием tasks.py.
from celery import shared_task
import time

# @shared_task
# def hello():
#     time.sleep(10)
#     print("Hello, world!")